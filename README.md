# gpt-inventory-tool
A GPT-powered tool to detect duplicate data. Supports the GPT-3.5 Turbo Model and Levenshtein distance model.
## Deployment
Needs to be updated

https://gpt-inventory-tool-production.up.railway.app/

## Naive Bayes Resources: 
https://www.bing.com/images/search?view=detailV2&ccid=CIo99cM8&id=191446FD20D2533F964F9087283B0E8B06002C4A&thid=OIP.CIo99cM8TpS6osouLdQ7vQHaFj&mediaurl=https%3A%2F%2Fimage1.slideserve.com%2F1652671%2Fbayes-theorem5-l.jpg&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.088a3df5c33c4e94baa2ca2e2dd43bbd%3Frik%3DSiwABosOOyiHkA%26pid%3DImgRaw%26r%3D0&exph=768&expw=1024&q=bayes+theorem&simid=607994565926060552&form=IRPRST&ck=607D00F0BA094601C63A3D9E88F3DA61&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11
https://khlam.github.io/bayes/
## Levenshtein Distance:
You for each string you can: 
Replace 
Delete
Insert

Each of this is 1 move. 

For example Levenshtien distance of Horse and ros is 3. 

Steps: 

Replace h with r: rorse
Delete second r: rose
Dlete e: ros 

There are many approaches to solving this. I am just importing the Levenshtein library for the demo.
https://en.wikipedia.org/wiki/Levenshtein_distance#Recursive
