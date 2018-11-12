import requests
import os,re,time,random
import subprocess
import tomd
def download_mp4(url,dir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    filename=str(dir)+'/1.mp4'
    with open(filename,'wb') as f:
        f.write(req.content)
def download_img(url,dir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    with open(str(dir)+'/thumb.png','wb') as f:
        f.write(req.content)
def download_pic(url,dir,filename):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name'}
    req=requests.get(url=url)
    if req.status_code==200:
        with open(str(dir)+'/'+str(filename)+'.jpg','wb') as f:
            f.write(req.content)
def random_ip():
    a=random.randint(1,255)
    b=random.randint(1,255)
    c=random.randint(1,255)
    d=random.randint(1,255)
    return(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
f = open("/Volumes/Untitled/video/test1.log",encoding='utf-8')
for line in f:
    try:
        line = line.lstrip()
        line = line.replace('\n','')
        #print(line)
        goods_list = line.split("/")
        pres=goods_list[len(goods_list) -1].split(".")
        pre="."+str(pres[len(pres) -1])
        filename = goods_list[len(goods_list)-1]
        key = re.sub('(中文字幕)|_C|gg999.cc-|206.108.51.3-|-720x400|0413xplanet|\\[javxxoocom\\]MP4|.mkv|.avi|.mp4|.MP4|.rmvb|\\[Thzla\\]','',filename)
        key = re.sub(r'F$|c$|full$|divx$|-C1$|-HD1srt$|-C$|AVI$|R1$|_C$|R$|r$|C$| +.*|[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+','',key)
        base_url='https://www.javbus2.pw/search/' + key + '&parent=ce'
        print(key)
        proxies = {'http':'127.0.0.1:1087','https':'127.0.0.1:1087'}
        get_page=requests.get(str(base_url),proxies=proxies)
        video_url=re.findall(r'<a class="movie-box" href="(.*?)">',str(get_page.content,'utf-8',errors='ignore'))
        if(len(video_url)>0):
          headers={'Accept-Language':'zh-CN,zh;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36','X-Forwarded-For':random_ip(),'referer':base_url,'Content-Type': 'multipart/form-data; session_language=cn_CN'}
          base_req=requests.get(video_url[0],headers=headers,proxies=proxies)
          tittle=re.findall(r'<h3>(.*?)</h3>',str(base_req.content,'utf-8',errors='ignore'),re.S)
          print(tittle)
          infos =re.findall(r'<div class="col-md-3 info">(.*?)</div>',str(base_req.content,'utf-8',errors='ignore'),re.S)
          img_url = re.findall(r'<a class="bigImage" href="(.*?)">',str(base_req.content,'utf-8',errors='ignore'))
          sample_url= re.findall(r'<a class="sample-box" href="(.*?)">',str(base_req.content,'utf-8',errors='ignore'))
          name = re.findall(r"<span style=\"color:#CC0000;\">(.*?)</span>",str(base_req.content,'utf-8',errors='ignore'),re.S)
          print(infos)
          print(name)
          info = tomd.Tomd(infos[0]).markdown
          #.replace('\r\n','')
          print(info)
          print(img_url)
          print(sample_url)
          try:
               t=tittle[0]
               tittle[0]=t.replace('\n','')
               t=tittle[0].replace(' ','')
               t=re.sub(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+','',t)
               t=t.replace('・','')
               print(t)
          except IndexError:
               pass
          readmeContent=''
          if os.path.exists(str(t))==False:
               try:
                   os.makedirs(str(t))
                   print('开始下载:'+str(t))
                   download_img(str(img_url[0]),str(t))
                   os.makedirs(str(t) + "/sample")
                   if(len(sample_url)>0):
                     filename=1
                     for download_url in sample_url:
                         print(download_url)
                         download_pic(str(download_url),str(t) + '/sample/',filename)
                         readmeContent = readmeContent + '![](http://oneindex.guibiaoguo.tk/?/onemac/'+str(t)+'/sample/'+str(filename)+'.jpg)' + '\n'
                         filename=filename+1
                   print('下载完成')
                   content = '###' + t + '\n' + info + '\n' + '![](http://oneindex.guibiaoguo.tk/?/onemac/'+str(t)+'/tunmb.png)'
                   with open(str(t)+'/'+'HEAD.md','w') as fw:
                    fw.write(content)
                   #result= subprocess.getoutput('sh /www/wwwroot/filemanage.com/www/file/91/autoupload.sh "' + '/www/wwwroot/filemanage.com/www/file/91/' + str(t) + '"')
                   #print(result)
                   #count = 1
                   #while count < filename:
                   #   readmeContent = readmeContent + '![](http://oneindex.guibiaoguo.tk/?/onemac/'+str(t)+'/sample/'+str(count)+'.jpg)' + '\n'
                   #   count = count + 1
                   with open(str(t)+'/'+'README.md','w') as fw2:
                     fw2.write(readmeContent)
                   result= subprocess.getoutput('rclone move '+'"'+str(t)+'" "remote:onemac/'+str(t)+'"')
                   print(result)
                   cmd='rclone move '+'"'+str(line)+'" "remote:onemac/'+str(t)+'"'
                   print(cmd)
                   result= subprocess.getoutput(cmd)
                   print(result)
               except:
                   pass
          else:
               print('已存在文件夹,跳过')
               time.sleep(2)      
      #break
    except:
        pass
f.close()
#flag=1
#while flag<=100:
#    tittle=[]
#    base_url='http://91porn.com/view_video.php?viewkey='
#    page_url='http://91porn.com/v.php?category=rf&viewtype=basic&page='+str(flag)
#    get_page=requests.get(url=page_url)
#    viewkey=re.findall(r'<a target=blank href="http://91porn.com/view_video.php\?viewkey=(.*)&page=.*&viewtype=basic&category=rf">\n                    <img ',str(get_page.content,'utf-8',errors='ignore'))
#    for key in viewkey:
#        headers={'Accept-Language':'zh-CN,zh;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36','X-Forwarded-For':random_ip(),'referer':page_url,'Content-Type': 'multipart/form-data; session_language=cn_CN'}
#        video_url=[]
#        img_url=[]
#        base_req=requests.get(url=base_url+key,headers=headers)
#        video_url=re.findall(r'<source src="(.*?)" type=\'video/mp4\'>',str(base_req.content,'utf-8',errors='ignore'))
#        tittle=re.findall(r'<div id="viewvideo-title">(.*?)</div>',str(base_req.content,'utf-8',errors='ignore'),re.S)
#        img_url=re.findall(r'poster="(.*?)"',str(base_req.content,'utf-8',errors='ignore'))
#        try:
#            t=tittle[0]
#            tittle[0]=t.replace('\n','')
#            t=tittle[0].replace(' ','')
#        except IndexError:
#            pass
#        if os.path.exists(str(t))==False:
#            try:
#                os.makedirs(str(t))
#                print('开始下载:'+str(t))
#                download_img(str(img_url[0]),str(t))
#                download_mp4(str(video_url[0]),str(t))
#                print('下载完成')
#                result= subprocess.getoutput('sh /www/wwwroot/filemanage.com/www/file/91/autoupload.sh "' + '/www/wwwroot/filemanage.com/www/file/91/' + str(t) + '"')
#                print(result)
#            except:
#                pass
#        else:
#            print('已存在文件夹,跳过')
#            time.sleep(2)
#    flag=flag+1
#    print('此页已下载完成，下一页是'+str(flag))