from errbot import BotPlugin, botcmd
import subprocess
import time
import os

user_token = os.environ.get('JENKINS_USER_TOKEN')
prj_token = os.environ.get('JENKINS_PRJ_TOKEN')
url = os.environ.get('JENKINS_URL')

exportboy_upload_url = 'http://' + user_token + '@' + url + '/view/exportboy/job/1_exportboy_create_upload_link_v2/buildWithParameters?token=' + prj_token + '&sequence_num='
exportboy_upload_last_consoleText = 'http://' + user_token + '@' + url + '/view/exportboy/job/1_exportboy_create_upload_link_v2/lastBuild/consoleText'

exportboy_download_url = 'http://' + user_token + '@' + url + '/view/exportboy/job/3_exportboy_create_download_link_v2/buildWithParameters?token=' + prj_token + '&sequence_num='
exportboy_download_last_consoleText = 'http://' + user_token + '@' + url + '/view/exportboy/job/3_exportboy_create_download_link_v2/lastBuild/consoleText'


class Jenkins(BotPlugin):
    @botcmd()
    def exportboy(self, msg, args):
        return "exportboy work!"

    @botcmd()
    def exportboy_help(self, msg, args):
        help_doc = """
            >> 產生上傳連結
            !exportboy upload NUMBER
            
            >> 產生下載連接
            !exportboy download NUMBER
            
            >> 數值格式，三位數，用以識別對應需求單
            NUMBER format: 001~111

            >> 資料匯出NUMBER數值請需相同，不重覆使用
            !exportboy upload 001
            !exportboy download 001
        """
        return help_doc

    @botcmd(split_args_with=None)
    def exportboy_upload(self, msg, args):
        full_url = exportboy_upload_url + args[0]
        p = subprocess.Popen(["curl", full_url ], stdout=subprocess.PIPE, text=True)
        p.wait(5)
        yield "Now working for upload link, please wait..."
        time.sleep(10)
        p1 = subprocess.Popen(["curl", exportboy_upload_last_consoleText ], stdout=subprocess.PIPE, universal_newlines=True, text=True)
        output, err = p1.communicate()
        yield output

    @botcmd(split_args_with=None)
    def exportboy_download(self, msg, args):
        full_url = exportboy_download_url + args[0]
        p = subprocess.Popen(["curl", full_url ], stdout=subprocess.PIPE, text=True)
        p.wait(5)
        yield "Now working for download link, please wait..."
        time.sleep(10)
        p1 = subprocess.Popen(["curl", exportboy_download_last_consoleText ], stdout=subprocess.PIPE, universal_newlines=True, text=True)
        output, err = p1.communicate()
        yield output
