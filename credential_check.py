import automationassets

print (automationassets.get_automation_variable("myvariable"))

cred = automationassets.get_automation_credential("mycredential")
print (cred['username'])
print (cred['password'])