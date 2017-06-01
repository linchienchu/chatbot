from transitions.extensions import GraphMachine
from lxml import etree, html
import random
import requests, json 
flag4=-1
flag5=-1
flag6=-1

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        flag=0
        if '心情' in text or '壓力' in text:
            flag=1
        return flag == 1

    def is_going_to_state2(self, update):
        text = update.message.text
        flag2=0
        if '去哪裡' in text or '玩' in text:
            flag2=1
        return flag2 == 1

    def is_going_to_state3(self, update):
        text = update.message.text
        flag3=0
        if '無聊' in text or '搞笑' in text or '短片' in text:
            flag3=1
        return flag3 == 1

    def is_going_to_state4(self, update):
        text = update.message.text
        global flag4
        if '0' in text :
            flag4=0
        elif '1' in text :
            flag4=1
        elif '2' in text :
            flag4=2
        elif '3' in text :
            flag4=3
        elif '4' in text :
            flag4=4
        elif '5' in text :
            flag4=5
        else:
            flag4=6
        return flag4 != -1

    def is_going_to_state5(self, update):
        text = update.message.text
        global flag5
        if '0' in text :
            flag5=0
        elif '1' in text :
            flag5=1
        elif '2' in text :
            flag5=2
        elif '3' in text :
            flag5=3
        elif '4' in text :
            flag5=4
        elif '5' in text :
            flag5=5
        else:
            flag5=6
        return flag5 != -1

    def is_going_to_state6(self, update):
        text = update.message.text
        global flag6
        if '0' in text :
            flag6=0
        elif '1' in text :
            flag6=1
        elif '2' in text :
            flag6=2
        elif '3' in text :
            flag6=3
        elif '4' in text :
            flag6=4
        elif '5' in text :
            flag6=5
        else:
            flag6=6
        return flag6 != -1

    def is_going_to_state7(self, update):
        text = update.message.text
        flag7=0
        if '好' in text or 'OK' in text or '有什麼' in text:
            flag7=1
        return flag7 == 1

    def is_going_to_state8(self, update):
        text = update.message.text
        flag8=0
        if '不' in text or 'No' in text or 'no' in text or 'NO' in text:
            flag8=1
        return flag8 == 1

    def on_enter_state1(self, update):
        update.message.reply_text("我想你可能心情不太好，以下選項有幾個符合你的情況？\n(輸入數字就好)\n1.常常覺得想哭\n2.心情不好\n3.比以前容易發脾氣\n4.睡不好\n5.不想吃東西\n")
        #self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("要不要來看個電影呢？")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("來看看有什麼好笑的短片吧~")
        number=0
        number= random.randint(1, 10)

        if number==1:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/17558400_1439295429438640_8581081320078180352_n.mp4?oh=afb3fc8f7ab607d24214ca42d56b9b77&oe=592EEA08')
            update.message.reply_text('我是不是按到直播...')
        elif number==2:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/13451691_1142591765814070_1096121320_n.mp4?oh=b3a7a3264515a7178de29c21f5754b95&oe=592F10E3')
            update.message.reply_text('被抓包的表情.....')
        elif number==3:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/12559397_1078738292183168_1789337302_n.mp4?oh=db779d010d8748bab0bc36683fcb3d6c&oe=592F0865')
            update.message.reply_text('這，我到底看了什麼？')
        elif number==4:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/17305179_1135295983260401_6330776429889847296_n.mp4?oh=cfe7fec251e2375c289f7727b166e2c2&oe=592F09F9')
            update.message.reply_text('你是在演哪齣~~~')
        elif number==5:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/11233348_998184620222345_689533516_n.mp4?oh=ba10fe7d601cb1d8b38c4ab6e639f7b1&oe=592F051B')
            update.message.reply_text('好奇嚇到喵~~')
        elif number==6:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/14144998_1131775566895540_79578518_n.mp4?oh=8cfdc9febe18887fe551f2dd67d853dc&oe=592F070D')
            update.message.reply_text('貓欺負狗，從小到大')
        elif number==7:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/18682544_1258061997624820_4916937702160465920_n.mp4?oh=b1aaf8a13c398e1bf3fb42404afa9e4e&oe=592F04AB')
            update.message.reply_text('偽裝術')
        elif number==8:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/18778446_1361161910604486_1287465005876248576_n.mp4?oh=d6d2c1242e7efbeb47d341e948139491&oe=592F1F7D')
            update.message.reply_text('陰影無限大')
        elif number==9:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/13404880_545198485605187_418041493_n.mp4?oh=525ba6e621a68cac14852600d08ae1af&oe=592F0C11')
            update.message.reply_text('魚是用來吃滴，不是拿來拍照滴')
        elif number==10:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/17346475_1261894057219587_8663157333355921408_n.mp4?oh=b88c70d73b86225afd67e2dba78fb66d&oe=592F068D')
            update.message.reply_text('順手牽羊的由來')
        else:
            update.message.reply_video(video='https://video-tpe1-1.xx.fbcdn.net/v/t42.4659-2/11968609_1090204964337827_267425306_n.mp4?oh=2de01ae7f057c28a34048c7a0dc89407&oe=592F0A97')
            update.message.reply_text('你在看什麼，就是這個...')
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("我看你最近有點壓力喔，以下選項有幾個符合你的情況呢？\n(輸入數字就好)\n1.一些無法預期的事發生而感到心煩\n2.感覺無法控制生活中重要的事\n3.覺得緊張不安\n4.無法處理惱人的生活麻煩\n5.無法有效地處理生活中發生的改變\n")
        #self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4 %d ~~' %(flag4)) 

    def on_enter_state5(self, update):
        update.message.reply_text("再問問最後一題，以下選項有幾個符合你的情況呢？\n(輸入數字就好)\n1.無法停止或控制憂慮\n2.過份擔憂不同的事\n3.很難放鬆\n4.心緒不寧甚至坐立不安\n5.容易心煩或易怒\n")
        #self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5 %d ~~' %(flag5))

    def on_enter_state6(self, update):
        update.message.reply_text("感謝你回答完我的問題!經由剛剛的你的回答，我大概分析出了你的狀況：")
        if flag4==0 or flag4==1:
            update.message.reply_text("有關你的憂鬱狀況，你目前的情緒狀態很穩定，是個懂得適時調整情緒及紓解壓力的人，繼續保持下去喔。")
        elif flag4==2:
            update.message.reply_text("有關你的憂鬱狀況，最近的情緒是否起伏不定？或是有些事情在困擾著你？\n處理方式：試著了解心情變化的緣由，做適時的處理，或許會比較有幫助喔~")
        elif flag4==3:
            update.message.reply_text("有關你的憂鬱狀況，有許多事壓在心上，肩上總覺得很沉重？因為你的壓力負荷量已到了臨界點了，千萬別再「撐」了！\n處理方式：趕快去找個朋友聊聊，心情找個出口，放下肩上的重擔吧！")
        elif flag4==4:
            update.message.reply_text("有關你的憂鬱狀況，現在的你必定感到相當不順心，無法展露笑容，一肚子苦惱及煩悶，連朋友也不知道如何幫忙。\n處理方式：或許可以試試找專業機構或心理師好好聊一下。")
        elif flag4==5:
            update.message.reply_text("有關你的憂鬱狀況，你是不是感到相當的不舒服，會不由自主的沮喪、難過，無法掙脫？因為心已「感冒」。\n處理方式：心病需要心藥醫趕緊到醫院找專業及可信賴的醫生檢查，透過他們的診療與治療，你將不再覺得孤單、無助！")
        else:
            update.message.reply_text("你的第一題輸入的題數有錯喔~或許等等可以再試一次")

        if flag5==0 or flag5==1:
            update.message.reply_text("接著，關於你最近的壓力，你目前的壓力感是輕微的，有時適度的壓力反而能激發更好的表現！")
        elif flag5==2:
            update.message.reply_text("接著，關於你最近的壓力，最近有一點壓力喔~\n處理方式：建議放慢工作與生活的步調，每天安排一些適合的放鬆活動，例如泡澡，聽音樂，閱讀，散步，緩和運動等~")
        elif flag5==3 or flag5==4:
            update.message.reply_text("接著，關於你最近的壓力，你目前處於高壓狀態喔~\n處理方式：建議適度調整工作量，或休個假讓自己喘息一下。同時，也要找家人或朋友訴苦，幫忙")
        elif flag5==5:
            update.message.reply_text("接著，關於你最近的壓力，壓力負荷沈重，影響身心健康~\n處理方式：建議找心理師或心身科醫師的稍微聊一下喔~")
        else:
            update.message.reply_text("你的第二題輸入的題數有錯喔~或許等等可以再試一次")

        if flag6==0 or flag6==1:
            update.message.reply_text("最後，你的焦慮程度，你幾乎不焦慮，恭喜你，是個從容自在的幸運兒！")
        elif flag6==2:
            update.message.reply_text("最後，你的焦慮程度，有一點輕微的焦慮\n處理方式：請試著放慢生活步調，練習深呼吸，泡個澡來放鬆一下吧！")
        elif flag6==3 or flag6==4:
            update.message.reply_text("最後，你的焦慮程度，對生活感到了不小的焦慮了\n處理方式：或許可以找朋友聊聊，同時試試看一些放鬆運動，例如慢跑、瑜珈或是柔軟操")
        elif flag6==5:
            update.message.reply_text("最後，你的焦慮程度，焦慮程度有些高\n處理方式：或許可以尋求專業心理師或身心科醫生的協助喔~")
        else:
            update.message.reply_text("你的第三題輸入的題數有錯喔~或許等等可以再試一次")

        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6 %d ~~' %(flag6))

    def on_enter_state7(self, update):
        update.message.reply_text("最近上映的電影有很多喔~")
        result = requests.get("https://tw.movies.yahoo.com/movie_intheaters.html")  
        result.encoding = 'utf8'
        root = etree.fromstring(result.content, etree.HTMLParser()) 
        jsonData = "像是"
        for row in root.xpath("//div[@class='text']/h4[position()>0]"):
            column = row.xpath("./a/text()")
            tmp= ' "%s" ,' % (column[0])
            jsonData += tmp
   
        update.message.reply_text(jsonData[0:-1] + '，挑一部來看吧！')

        self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')

    def on_enter_state8(self, update):
        update.message.reply_text("好吧~")
        self.go_back(update)    

    def on_exit_state8(self, update):
        print('Leaving state8 ' )

