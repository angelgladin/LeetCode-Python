# 721. Accounts Merge
# https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(stack, emails, explored, graph):
            while stack:
                u = stack.pop()
                emails.append(u)
                for v in graph[u]:
                    if v not in explored:
                        explored.add(v)
                        stack.append(v)
        
        graph = defaultdict(set)
        email_to_name = dict()
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email_to_name[account[i]] = name
                if i == 1:
                    continue
                graph[account[i]].add(account[i-1])
                graph[account[i-1]].add(account[i])

        explored = set()
        ans = []
        for email in email_to_name.keys():
            if email not in explored:
                explored.add(email)
                stack = [email]
                emails = []
                dfs(stack, emails, explored, graph)
                emails.sort()
                ans.append([email_to_name[email]] + emails)
        return ans
