import socket
import sys

server = "irc.servercentral.net"       #settings
channel = "#spudchat"
botnick = "PotatoBot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print("connecting to: " + server)
irc.connect((server,6669))                                                         #connects to the server
irc.send("USER "+botnick+": This is a fun bot!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ channel +"\n")        #join the chan

        
def prvtmsg(reciever,msg):
    irc.send("PRIVMSG "+reciever+" :" +msg+ "\r\n")
def msg(msg):
    irc.send("PRIVMSG "+channel+" :" +msg+ "\r\n")
def ping():
    msg("pong")


while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
   print(text)#print text to console
   if text.find('PING')!= -1:                          #check if 'PING' is found
       irc.send('PONG ' + text.split()[1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
   if text.find('!potato') !=-1: #you can change !hi to whatever you want
       t = text.split('!potato') #you can change t and to :)
       to = t[1].strip() #this code is for getting the first word after !hi
       try:
           exec(to)
       except:
           msg("Error!")
       #irc.send('PRIVMSG '+channel+' : '+str(to)+'! \r\n')
