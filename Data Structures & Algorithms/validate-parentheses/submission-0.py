class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)%2!=0:
            return False
        else:
            for i in s:
                if i in "{[(":
                    stack.append(i)
                elif i in "}])" and len(stack)!=0:
                    if stack[len(stack)-1]=="(" and i==")":
                        stack.pop()
                    elif stack[len(stack)-1]=="{" and i=="}":
                        stack.pop()
                    elif stack[len(stack)-1]=="[" and i=="]":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if len(stack)==0:
                return True
            else:
                return False
        