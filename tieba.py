#coding:utf-8
import  requests
import time
import smtplib
import poplib
from email.mime.text import MIMEText


'''post请求'''
def sguTieBa(content):
    posturl='http://tieba.baidu.com/f/commit/post/add'
    # print content
    cookie='BAIDUID=7110EDE6A8C08452263F2A54E9F5C4F5:FG=1; BIDUPSID=7110EDE6A8C08452263F2A54E9F5C4F5; PSTM=1465223427; TIEBA_USERTYPE=dd9cfee96af3dd6677f722e4; bdshare_firstime=1470544613174; TIEBAUID=a5de5c0adc867638b33b4c06; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; H_PS_PSSID=1435_18241_17945_11466_20847_20857_20836_20771; wise_device=0; LONGID=2143580469; BDUSS=Xk0aXc4OEV5M0ZCOEJjNmk2bEd3eWl6MUE0V1dNaHBTQWktQWNKUHVxa1hJZHBYQVFBQUFBJCQAAAAAAAAAAAEAAAA1ccR~YWxlcnRaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABeUslcXlLJXN'
    # print cookie
    headers={
             'Host': 'tieba.baidu.com',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
             'Accept': 'application/json, text/javascript, */*; q=0.01',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding': 'gzip, deflate',
             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'X-Requested-With': 'XMLHttpRequest',
             'Referer': 'http://tieba.baidu.com/p/4707820447?pn=2',
             'Content-Length': '613',
             'Cookie':cookie,
             'Connection': 'keep-alive'
             }
    data={
         'ie':'utf-8',
         'kw':'韶关学院',
         'fid':'123118',
         'tid':'4707820447',
         'vcode_md5':'',
         'floor_num':49,
         'rich_text':1,
         'tbs':'e86cdcbc24aa53371471321113',
         'content':content,
         'files':'[]',
         'mouse_pwd':'99,106,105,118,107,111,106,111,83,107,118,106,118,107,118,106,118,107,118,106,118,107,118,106,118,107,118,106,83,104,110,109,99,98,83,107,99,104,106,118,107,106,98,106,14713211051900',
         'mouse_pwd_t':'1471321105190',
         'mouse_pwd_isclick':0,
         '__type__':'reply'

    }
    # print urllib.urlencode(data)
    r=requests.post(posturl,data=data,headers=headers)
    # print r.json()
    result=dict(r.json())
    return result[u'err_code']

'''提取要发送的内容'''
def theData(time):
    toSendData={
                16:u'准时冒一下泡！by the way 我叫小号 ^_^',
                17:u'收到来自小号的调戏，你接受吗？',
                18:u'嘿嘿，小鲜肉看过来。这里很精彩哦！（不要回此贴，老板会骂我的:)）',
                19:u'又是一天了，小号在极光等着各位的到来哦！',
                20:u'曾经,有一份真挚的\'爱情\'摆在我面前,我没有好好珍惜,等到我失去的时候才后悔莫及...',
                21:u'没错,我是小号，想成为大神吗？赶紧加极光工作室交流群吧！群号:539365225',
                22:u'想成为大神吗？想让代码在你的指尖飞跃吗？别犹豫了，赶紧拿起手机加群吧！(ps:群号里面有)',
                23:u'小号例行插楼，我只是个机器人，别摸我头！',
                24:u'还有人没睡吗？过来吧，和小号面基吧！',
                25:u'啦啦啦，还没睡的小伙伴，下一个大神就是你了！',
                26:u'临近开学了，不知道各位新鲜肉有什么想法呢？路过的快进来看看啊，小号要开车了！',
                27:u'手打很累的，没人么？没人我可睡了:(',
                28:u'嘿，没错是我小号，你们都睡了吗？没人陪我玩啊:(',
                29:u'马上要开学了，很快就能见到新鲜滚烫烫的小鲜肉了，好嗨心！！',
                30:u'程序员你还怕没对象吗？new一个吧!',
                31:u'九月快到了，你们还会远吗？快到碗里来！！',
               }
    return toSendData[time]

'''发邮件'''
def send_mail(tolist,sub,content):
    me='self'+'<'+mail_usr+'@'+mail_postfix+'>'
    msg=MIMEText(content,_subtype='palin',_charset='utf-8')
    msg['Subject']=sub
    msg['From']=me
    msg['To']=';'.join(tolist)
    try:
        server=smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_usr,password)
        server.sendmail(me,tolist,msg.as_string())
        server.close()
        return True
    except Exception,e:
        print str(e)
        return False


'''发送回执邮件给我'''
def sendEmailToMe(resultcode,data,message=u'报告老板，帖子发送成功:)'):

    if resultcode==0:
         sub=message+u'发帖的内容为:'+data
    else:
         sub=u'噢！I\'m sorry Boss,发生了未知的错误，发帖失败!:('
    send_mail(mailto_list,sub,'')

if __name__=='__main__':
     host = 'pop.sina.com'
     mail_host='smtp.sina.com'
     username = 'zallensmith@sina.com'
     password = 'iamallensmith'
     mail_usr='zallensmith'
     mail_postfix='sina.com'
     mailto_list=['729889375@qq.com']
     print 'Tieba.py is running.....'
     while(True):
          nowDay=time.strftime("%d",time.localtime())
          nowHour=time.strftime("%H",time.localtime())
          nowMinute=time.strftime("%M",time.localtime())
          nowSeconds=time.strftime("%S",time.localtime())
           
          nowDay=int(nowDay)
          nowHour=int(nowHour)
          nowMinute=int(nowMinute)
          nowSeconds=int(nowSeconds)
          
          #早
          if nowHour==9 and nowMinute==29 and nowSeconds==1:
                data=theData(nowDay)
                # 发送帖子
                resultcode=sguTieBa(data)
                # 判断发送帖子的返回码，发送邮件通知
                sendEmailToMe(resultcode,data)
                time.sleep(2)

          #中
          if nowHour==14 and nowMinute==30 and nowSeconds==1:
                data=theData(nowDay)
                # 发送帖子
                resultcode=sguTieBa(data)
                # 判断发送帖子的返回码，发送邮件通知
                sendEmailToMe(resultcode,data)
                time.sleep(2)

          #晚
          if nowHour==19 and nowMinute==31 and nowSeconds==1:
                data=theData(nowDay)
                # 发送帖子
                resultcode=sguTieBa(data)
                # 判断发送帖子的返回码，发送邮件通知
                sendEmailToMe(resultcode,data)
                time.sleep(2)
          #凌晨
          if nowHour==0 and nowMinute==32 and nowSeconds==1:
                data=theData(nowDay)
                # 发送帖子
                resultcode=sguTieBa(data)
                # 判断发送帖子的返回码，发送邮件通知
                sendEmailToMe(resultcode,data)
                time.sleep(2)

          if nowDay==1:
              exit(1)

