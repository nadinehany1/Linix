import facebook

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "https://www.facebook.com/nadinhanyy/"      : "VALUE",  # Step 1
    "EAATrfHQNlSABAOMlrRKSZCfQBPZBKZB5HL2cuPkIygSTQxogwaHZBcmbOa5iImpIZBxTUm5bxwGPXV5Cm10jRvSuooSVKJ2DrR6qqQ15UxmdmHlilWkBfbrixDMI85EJvLDFpa5apg3B1dkyYvLgge3gN182fEh7BUATOvcc3eJ4tVMs2SSDELtqmgW9e0RZBH2MwmqZCAgXZCTaDRZAoOMOFVD9By4roI5ZAruMpLQCTe9Mn1tZBilE1ZAP" : "VALUE"   # Step 3
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['EAATrfHQNlSABAOMlrRKSZCfQBPZBKZB5HL2cuPkIygSTQxogwaHZBcmbOa5iImpIZBxTUm5bxwGPXV5Cm10jRvSuooSVKJ2DrR6qqQ15UxmdmHlilWkBfbrixDMI85EJvLDFpa5apg3B1dkyYvLgge3gN182fEh7BUATOvcc3eJ4tVMs2SSDELtqmgW9e0RZBH2MwmqZCAgXZCTaDRZAoOMOFVD9By4roI5ZAruMpLQCTe9Mn1tZBilE1ZAP'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['EAATrfHQNlSABAOMlrRKSZCfQBPZBKZB5HL2cuPkIygSTQxogwaHZBcmbOa5iImpIZBxTUm5bxwGPXV5Cm10jRvSuooSVKJ2DrR6qqQ15UxmdmHlilWkBfbrixDMI85EJvLDFpa5apg3B1dkyYvLgge3gN182fEh7BUATOvcc3eJ4tVMs2SSDELtqmgW9e0RZBH2MwmqZCAgXZCTaDRZAoOMOFVD9By4roI5ZAruMpLQCTe9Mn1tZBilE1ZAP']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  main()