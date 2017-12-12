#coding=utf-8

relStrs={'ADJECTIVE','NOUN','ADVERB','VERB'}
rDemo=open('demo.txt')
demo = str(rDemo.readlines())
print demo
rDemo.close()
newDemo=demo
for i in range(len(demo)):
    for j in range((len(demo))-i):
        if demo[i:(i+j)] in relStrs:
            relStr=raw_input('Enter an '+demo[i:(i+j)]+':\n')
            newDemo=newDemo.replace(demo[i:(i+j)],relStr)
newDemo = newDemo.lstrip('\[\'')
newDemo = newDemo.rstrip('\'\]')
testDemo = open('demoNew.txt','w')
testDemo.write(newDemo)
testDemo.close()
rDemo=open('demoNew.txt')
print str(rDemo.readlines())
rDemo.close()