class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_id = {}
        email_name = {}
        curr_id = 0
        
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in email_id:
                    email_id[email] = curr_id
                    curr_id += 1
                    email_name[email] = name
            
        parents = [i for i in range(curr_id)]
        ranks = [1 for i in range(curr_id)]

        def find(num):
            while num != parents[num]:
                parents[num] = parents[parents[num]]
                num = parents[num]
            
            return num
        
        def union(a, b):
            first, second = find(a), find(b)

            if first == second: return

            if ranks[first] > ranks[second]:
                parents[second] = first
                ranks[first] += ranks[second]
            else:
                parents[first] = second
                ranks[second] += ranks[first]
            
            return
        
        #group accounts by row by having them point at base_email as parent
        for account in accounts:
            name = account[0]
            base_email = email_id[account[1]]

            for email in account[2:]:
                union(base_email, email_id[email])
        
        root_email_rows = {}
        for email, e_id in email_id.items():
            root = find(e_id)
            if root not in root_email_rows:
                root_email_rows[root] = []
            root_email_rows[root].append(email)
        
        res = []
        for root, emails in root_email_rows.items():
            name = email_name[emails[0]]
            emails.sort()
            res.append([name] + emails)
        
        return res
