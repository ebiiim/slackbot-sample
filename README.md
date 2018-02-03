# A Slack Bot Written in Python
[Slack Developer Kit for Python](https://slackapi.github.io/python-slackclient/)を使ってbotっぽいサンプルを作りました

## Usage

1. `$ clone https://github.com/ebiiim/slackbot-sample.git; cd slackbot-sample`
1. `$ pip install -r requirements.txt`
1. Slack workspaceにbot userを追加します
1. 追加したbot userのAPI Token記載したsecret.tomlをルートディレクトリに追加します
1. `$ python run.py`
1. Slackでbotにメンションを送ります(`@your_bot help` `@your_bot 使い方`)
1. Create your own bot!

## kwsk

### 1. Clone this repo
`$ clone https://github.com/ebiiim/slackbot-sample.git; cd slackbot-sample`

### 2. Install requirements
 `$ pip install -r requirements.txt`

### 3. Add a bot user
[Bot Users - Slack](https://api.slack.com/bot-users)にある[creating a new bot user](https://my.slack.com/services/new/bot)のリンクをクリックします。

![](./docs/fig1.png)

botに名前を付けたら`Add integration`をクリックします。

![](./docs/fig2.png)

### 4. secret.toml

API Tokenを以下のように`secret.toml`に書いてルートディレクトリに保存します。

```toml:secret.toml
[slack]
api_token = 'xoxb-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX'
```

![](./docs/fig3.png)

### Start bot
`$ python run.py`

### Send a command

botをチャンネルに追加してあげないと発言できないです。

![](./docs/fig4.png)

お好みのコマンドを追加してください。

![](./docs/fig5.png)

## Reference
- 全体的にこちらを参考にしました [How to Build Your First Slack Bot with Python - Full Stack Python](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)
- TOMLの存在を知りました [inokappa/slack_bot-python](https://github.com/inokappa/slack_bot-python)
