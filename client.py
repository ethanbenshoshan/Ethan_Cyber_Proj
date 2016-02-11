#imports

#class communication_client:
    #open socket recieve buffer

class File_Manager:
##    class _File_Manager:
##        def __init__(self, arg):
##            self.val = arg
##        def __str__(self):
##            return repr(self) + self.val
##    instance = None
##    def __init__(self, arg):
##        if not File_Manager.instance:
##            File_Manager.instance = File_Manager.File_Manager(arg)
##        else:
##            File_Manager.instance.val = arg
##    def __getattr__(self, name):
##        return getattr(self.instance, name)
  
    def Read_File_Magicnumbers():
        #file will be found by hooking
        f=open("C:\Users\User\Desktop\ethan.docx", "rb")
        x=f.read(20)
        x=x.encode("hex")
        print x
        answer=Policy_Manager.File_Identifier(x)
        Enforcer_Client.Enforce_Policy(answer)
        
        
    
class Enforcer_Client:
    
    def Enforce_Policy(answer):
        #if file type is allowed, will allow user to open, if not will block user from opening
        if answer == True:
            #program will allow file to be opened
        else:
            #program will block file
        
        
#class log_manager:
#keeps history of files that were blocked 

    
        
#class Encryption_manager:



#class login_client:


class Policy_Manager:
    File_Type_Policy={'Allowed':['JPG/JPEG', 'GIF', 'rar', 'mp3'], 'Disallowed':['docx', 'exe', 'pdf']}
    File_Signatures={'JPG/JPEG': ["ffd8ffdb", "ffd8ffe0", "ffd8ffe1"], 'docx/zip/jar':["504b"], 'GIF':["47 49 46 38"], 'exe':["4d5a"], 'rar':["526172211a07"], 'pdf':["25504446"], 'mp3':["fffb", "494433"]]}
##    class _Policy_Manager:
##        def __init__(self, arg):
##            self.val = arg
##        def __str__(self):
##            return repr(self) + self.val
##    instance = None
##    def __init__(self, arg):
##        if not Policy_Manager.instance:
##            Policy_Manager.instance = Policy_Manager.Policy_Manager(arg)
##        else:
##            Policy_Manager.instance.val = arg
##    def __getattr__(self, name):
##        return getattr(self.instance, name)

    
    def File_Identifier(magic):
        for x, y in File_Signatures.iteritems():
            if magic in y:
                print "file is of type " + x
                File_Policy(x)

    def File_Policy(file_type):
        for x, y in File_Type_Policy.iteritems():
            if file_type in y:
                if x=="Allowed":
                    return True
                elif x=="Disallowed":
                    return False

    def Update_File_Signatures:
        #function will update file signatures by server's command

    def Update_File_Type_Policy:
        #function will update file policy by server's command
                    
               
               
                
    
                
        
        
        
    
  
    

    
            
        
               
    
    
   
    
