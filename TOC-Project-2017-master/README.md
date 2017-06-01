# THEORY OF COMPUTATION Final Project 2017

chatbot name�G     ading(���B)
chatbot username�G a_ding_bot
�D�D�G�M�߲z���d��������Ѿ����H

## How to run my code

### �ާ@����
* �������GOracle VM VirtualBox
* Ubuntu Linux 32�줸

### Python����
* Python 3

### requirements.txt���e
Flask==0.12.1
transitions==0.5.0
pygraphviz==1.3.1
python-telegram-bot==5.3.0

### Step1 Install Dependency
```sh
sudo pip3 install -r requirements.txt
```
* �ݦw�� pygraphviz�M?transitions?�H��Flask�Mpython-telegram-bot�Mngrok
* ���٦��t�~��telegram Desktop https://desktop.telegram.org/ ?������linux 32bit

### Step2 Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.

### Step3 Run ngrok
1.�ݥӽбb���A�U��ngrok
2.�}��terminal

```sh
./ngrok authtoken token
```
* token �O�A�ӽЪ�

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a `https` URL.

You should set `WEBHOOK_URL` (in app.py) to `'your-https-URL/hook`.

### step4 Run the sever
* �i�J�M�ת���Ƨ�
```sh
python3 app.py
```
### step5 Run telegram�A�M��}�l���
�ڬO��telegram Desktop�A�bterminal�W����
```sh
./Telegram
```
## How to interact with my chatbot

### Finite State Machine
![fsm](./img/show-fsm.png)

### �p��i�Jstate1
�D�D�G�\��O�Ʊ����U�ϥΪ̧P�_��U���߱��A�õ�����ĳ
��J�]�t'�߱�'��'���O'���@�y�ܡA�Ǧp�߱����n�����O�ܤj�A�|�i�Jstate1
�M������H�|�ݧA����߱��q�����D�A�^�����|�i�Jstate4�������������D�b�i�Jstate5�M��state6
state6�|���ϥΪ̨̨Ǥ߱��W����ĳ�A�M��^��user

### �p��i�Jstate2
�D�D�G�\��O�Ʊ�ϥΪ̯�X�h�����A�ñ��ˤ@�ǤW�M�����q�v
��J�]�t'�h����'��'��'���@�y�ܡA�Ǧp�̪�n�h���̪��A�|�i�Jstate2
�����H�|�ݷQ���Q�ݹq�v�A�p�G�^���]�t'�n'��'OK'��'������'���@�y�ܡA�Ǧp������q�v
�|�i�Jstate7�A�����H�|�h�W�����Χ쥿�b�W�M�����q�v���W
�p�G�^���]�t'��'��'No'��'no'��'NO'���@�y�ܡA�|�i�Jstate8�A�M������H�|�^��'�n�a'�A�M��^��user

### �p��i�Jstate3
�D�D�G�\��O�Ʊ�༽��@�Ƿd���u���A���U�ϥΪ��V��
��J�]�t'�L��'��'�d��'��'�u��'���@�y�ܡA�Ǧp���̪�n�L��
�|�i�Jstate3�A�����H�|�ǰe�@�Ƿd���u���A�M��^��user

## Author
F74032049 �L�d�� 

