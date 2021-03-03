# Flask Vercel Template

Template repo for creating flask apps on [Vercel](https://vercel.com/) (previously Now).  
This repo contains minimal boilerplate to get your application going.  

## Example endpoints

You can start the dev server by running `vercel dev` on the root of the repo. Then you can try to hit the following endpoints:

```bash
$ curl -H "Content-Type: application/json" -d '{"name": "ajpl"}' -X POST http://localhost:3000/
{"hello":"ajpl"}
$ curl -H "Content-Type: application/json" -d '{"x": 23, "y": 21}' -X POST http://localhost:3000/add
{"result":44}
```

## More info

[Vercel Docs](https://vercel.com/docs)  
[Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)