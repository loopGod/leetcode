'''
10.6 Restore IP Addresses
描述
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example: Given ”25525511135”,
return [”255.255.11.135”, ”255.255.111.35”]. (Order does not matter)
'''
class Solution:
    def __init__(self):
        self.count=0
    # @return a list of lists of string
    def restoreIpAddresses(self, s):
        def dfs(s, sub, ips, ip):
            if sub == 4:                                        # should be 4 parts
                if s == '':
                    ips.append(ip[1:])                          # remove first '.'
                return
            for i in range(1, 4):                               # the three ifs' order cannot be changed!
                if i <= len(s):                                 # if i > len(s), s[:i] will make false!!!!
                    if (int(s[:i]) <= 255 and s[0]!='0') or int(s[:i])==0:
                        dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
                    #if s[0] == '0': break                       # make sure that res just can be '0.0.0.0' and remove like '00'
            print(ip+'.'+s[:i])
        ips = []
        dfs(s, 0, ips, '')
        return ips

s='25524511035'
mySolu=Solution()
res=mySolu.restoreIpAddresses(s)
print(res)

