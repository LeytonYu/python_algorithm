import openai
openai.organization = "org-5f80BJ9h4ytFWKCet99Lyf5Q"
openai.api_key = "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"
res = openai.Model.list()
print(res)