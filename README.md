# THEORY OF COMPUTATION Final Project 2017

chatbot name：     ading(阿丁)
chatbot username： a_ding_bot
主題：和心理健康有關的聊天機器人

## How to run my code

### 操作環境
* 虛擬機：Oracle VM VirtualBox
* Ubuntu Linux 32位元

### Python版本
* Python 3

### requirements.txt內容
Flask==0.12.1
transitions==0.5.0
pygraphviz==1.3.1
python-telegram-bot==5.3.0

### Step1 Install Dependency
```sh
sudo pip3 install -r requirements.txt
```
* 需安裝 pygraphviz和 transitions 以及Flask和python-telegram-bot和ngrok
* 我還有另外載telegram Desktop https://desktop.telegram.org/  版本為linux 32bit

### Step2 Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.

### Step3 Run ngrok
1.需申請帳號，下載ngrok
2.開啟terminal

```sh
./ngrok authtoken token
```
* token 是你申請的

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a `https` URL.

You should set `WEBHOOK_URL` (in app.py) to `'your-https-URL/hook`.

### step4 Run the sever
* 進入專案的資料夾
```sh
python3 app.py
```
### step5 Run telegram，然後開始對話
我是用telegram Desktop，在terminal上執行
```sh
./Telegram
```
## How to interact with my chatbot

### Finite State Machine
![fsm](./Desktop/show-fsm.png)


## Author
[Lee-W](https://github.com/Lee-W)

