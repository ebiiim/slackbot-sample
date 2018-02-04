import time
from slackclient import SlackClient
import logging
import toml

# 設定ファイル
CONFIG = toml.load(open('config.toml', encoding='utf-8'))
SECRET = toml.load(open('secret.toml', encoding='utf-8'))

# 認証後に代入する
bot_id = None

# ログの設定(ログはコンソールに表示する)
logging.getLogger().setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logging.getLogger().addHandler(ch)

sc = SlackClient(SECRET['slack']['api_token'])


def handle_cmd_kill(cmd):
    """
    killコマンドの処理を行うメソッド
    :param cmd: botにメンションで送ったメッセージ
    :return: Slackに投稿するメッセージ
    """
    cmds = cmd.split()
    if len(cmds) > 1:
        if cmds[1] in ['you', 'お前']:
            return CONFIG['bot']['res_kill_you']
    return CONFIG['bot']['res_kill']


def handle_command(cmd, channel):
    """
    botに対するメンションを処理するメソッド, コマンドの識別および処理の実施を行う
    :param cmd: コマンド(botに対するメンション)
    :param channel: Slackの対象チャンネル
    :return: サーバの応答(Slackの対象チャンネルにコマンドの実行結果を投稿した結果)
    """
    response = CONFIG['bot']['res_default']
    if cmd.startswith(('help', '-h', '--help', '使い方', 'a')):
        response = CONFIG['bot']['res_help']
    elif cmd.startswith('kill'):
        response = handle_cmd_kill(cmd)

    return sc.api_call('chat.postMessage', channel=channel, text=response, as_user=True)


def parse_slack_cmd(cmd):
    """
    RTM(Real Time Messaging) APIで受け取ったメッセージをパースするメソッド, botに対するメンションのみを認識する
    :param cmd: RTMで受け取ったJSON
    :return: (botに対するメンション, 対象チャンネル)
    """
    at_bot = '<@' + bot_id + '>'
    for elem in cmd:
        logging.debug("Parsing: " + str(cmd))
        if ('text' in elem) and (at_bot in elem['text']):
            return elem['text'].split(at_bot)[1].strip(), elem['channel']
    return None, None


if __name__ == '__main__':
    RTM_READ_DELAY = CONFIG['common']['rtm_interval']
    if sc.rtm_connect():
        logging.info('Bot connected and running!')
        bot_id = sc.api_call("auth.test")["user_id"]  # botのuser IDを取得する
        while True:  # コマンド待ち
            cmd, channel = parse_slack_cmd(sc.rtm_read())
            if cmd and channel:
                logging.info(str(handle_command(cmd, channel)))
            time.sleep(RTM_READ_DELAY)
    else:
        logging.warning('Connection failed.')
