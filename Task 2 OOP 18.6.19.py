# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:00:04 2019

@author: Hashim
"""

'''Task 2'''
#

class VideoApp:
    participants_online = 0
    action = ["speaking" "silent"]
 #   action = ["speaking" "silent"]
    def __init__(self, user_name=None, company=None):         #user_name and company are attributes
    #    self.participants_online = participants_online
    #    self.action = action
        self.user_name = user_name             #these are attributes, user_name and company
        self.company = company
#        self.participants_online = participants_online
 #       self.action= action
    
    #@classmethod                                
    def show_participants_online(cls, participants_online):              #this class method return the number of participants online
        return f'Online participants are {cls.participants_online}'
    
    #methods
    def go_online(self, participants_online):
        self.participants_online += 1
        
    def go_offline(self, participants_online):
        _participants_online = self.participants_online - 1
        return "Participants_online are {}".format(_participants_online)
    
    def status(action, user_name):
        if action != "speaking" or action!="silent":
            print("The user must either be speaking or silent")
            print(f"{user_name} is action")

class Message():
    def __init__(self,user_name, message):    
        self.user_name = user_name
        self.message = message
    
    def __status__(self):
        return f'{self.user_name} sent the message {self.message}'
        return "{} sent the message {}".format(self.user_name, self.message)

class ChatApp(VideoApp, Message):     ###Inhertitence
    def __init__(self):
        super(ChatApp, self).__init__()
        Message.__status__(self)   ###instance
                



'''Task 3'''

class Compare():
    def __new__(cls, *args, **kwargs):
        print("We are comparing string lengths.")
        str1 = super(Compare, cls).__new__(cls)#, *args, **kwargs)
        str2 = super(Compare, cls).__new__(cls)#, *args, **kwargs)
        #return len(str1) == len(str2)
 
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def __repr__(self):
        return 'Object 1 is: {}'.format(self.str1)
        return 'Object 2 is: {}'.format(self.str2)
    
a = Compare('ello')
b = Compare('Hi')
print(a==b)



''' Task 4'''

#from collections import namedtuple
#class PersonalJoiner:
#    def some_method(self):
#        pass

#class PersonalDetails:
#    def __init__(self):
       
'''useful link https://pymotw.com/2/collections/namedtuple.html'''


from collections import namedtuple
class PersonalJoiner:
    @staticmethod
    def join_(*args):
        d = {}
        for i in args:
            d.update(i.__asdict())
            person =  namedtuple('person', sorted(d))
            Person = person(**d)
        return Person

PersonalDetails = namedtuple('PersonalDetails', 'date_of_birth')#[, verbose=False][, rename=False])
person_1_details = PersonalDetails(date_of_birth = '09-04-1991')
person_features = namedtuple('person_features', 'eye_colour IQ_score')
person_1_features = person_features(eye_colour = 'green', IQ_score = 109)
person_ = PersonalJoiner()
print(PersonalJoiner.join_(person_1_details, person_1_features))


from collections import namedtuple
PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
person_features = namedtuple('person_features', ['eye_color', 'IQ_score'])

person_1_detail = PersonalDetails(date_of_birth='09-04-1991')
person_1_features =person_features(eye_color='green eyes', IQ_score=109)
#per = PersonalJoiner.join_(person_1_detail, person_1_features)

class PersonalJoiner:
   @staticmethod
   def join_(*args):
       d = {}

       for i in args:
           d.update(i._asdict())
           person=namedtuple('person', d)
           Person= person(**d)
       return Person

person_= PersonalJoiner()
print(PersonalJoiner.join_(person_1_detail, person_1_features))


m = {"k":"a" , "l":"b"}
#n = {"k":"c" , "l":"d"}
def meth(k={}, l={}):
    return k,l
meth(*m)
#meth(**m, **n)    #Unpacking of all the dictionary parameters
#meth(*m, *n)
#meth(m,n)


'''Task5'''

def double(ip_funct):
    #ip = input ("Please provide the input kyword argument:")
    def inner():
       ip_funct()
       #ip_funct()  
        #lst = [ip_funct(),ip_funct()]
    return inner

@double
def ip_funct():
    x= "Ditto"
    lng = len(x)
    print(lng)
#list = [x for i in range(lng)]
    for i in range(lng):
        list = [x]*i
        list.append(x)
    print (list)
ip_funct()




'''Task6'''

def verify(ip_funct):
    ip = input ("Please provide the input kyword argument:")
    def inner():
        if ip == 'role:admin':
            print("Kaisay kar letey ho yar, kya baat hai?")
            ip_funct()
        else:
            print("Invalidation")
    return inner


@verify
def ip_funct():
    print ("The function is being called properly here.")
ip_funct()
          



kw= {'a':5.5}
def ttry( b=2, *arg, **kw):
    if 'a'in kw:
        a = kw['a']
    return a
ttry(b=kw)
ttry(**{'d':2})
#ttry([1,2], kw)
#ttry(a=2, *[1,2], kw)
#ttry(*[1,2])

#i = Compare("Hi","Hello")
    
#    def __init__(self, stringg):
#        self.stringg = stringg
        
        
        
class Foo(object):
    def __new__(cls, *args, **kwargs):
        print ("Creating Instance")
        instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return instance
 
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
 
    def bar(self):
        pass
i =Foo(2,3)


        
        
        
        
        