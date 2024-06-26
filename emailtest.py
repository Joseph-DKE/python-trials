import re
import smtplib
import dns.resolver

# Get domain for DNS lookup
addressToVerify="etsejoey@gmail.com"
splitAddress = addressToVerify.split('@')
domain = str(splitAddress[1])
print('Domain:', domain)

# MX record lookup
records = dns.resolver.resolve(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)


# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
fromAddress="etsejoey@yahoo.com"
server.mail(fromAddress)
code, message = server.rcpt(str(addressToVerify))
server.quit()

#print(code)
#print(message)

# Assume SMTP response 250 is success
if code == 250:
   print('Success')
else:
   print('Bad')