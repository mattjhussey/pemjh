import sys
import time
import os

try:
    import psyco
    psyco.full()
    print "Psyco working"
except:
    pass

def testFunction(id, func, knownAnswer):
    result = 2 # 0 = correct, 1 = wrong, 2 = not known
    profile = time.clock()
    answer = func()
    profile = time.clock() - profile
    print "c%d(%2.6f):\t" % (id, profile), answer,
    if not knownAnswer == None:
        if (knownAnswer == answer):
            print "\tCorrect"
            result = 0
        else:
            print "\tWrong. Should be %d" % knownAnswer
            result = 1
    else:
        print

    return result

wholeTime = time.clock()

failures = list()    

nChallenges = 0
for i in xrange(1, 300):
    package_name = "challenge%03d" % i

    if os.path.exists("%s/%s" % (os.getcwd(), package_name)):
        try:
            sys.path.append(package_name)
            mod = __import__(package_name)
        
            func = getattr(mod, package_name)

            if hasattr(mod, "answer"):
                knownAnswer = mod.answer
            else:
                knownAnswer = None

            if hasattr(mod, "desc"):
                print mod.desc

            if testFunction(i, func, knownAnswer) == 1:
                failures.append(package_name)
            nChallenges += 1
        except ImportError as err:
            print "Import Error %s %s" % (package_name, err)
        

wholeTime = time.clock() - wholeTime
print "Completed in %g" % wholeTime
if nChallenges > 0:
    print "Average time of %g per challenge" % (wholeTime / nChallenges)

if len(failures) > 0:
    print "Failures:"
    for fail in failures:
        print fail
