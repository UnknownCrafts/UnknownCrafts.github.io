(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[49706,53950,65410],{7110:e=>{"use strict";function s(e){e.languages.json={property:{pattern:/(^|[^\\])"(?:\\.|[^\\"\r\n])*"(?=\s*:)/,lookbehind:!0,greedy:!0},string:{pattern:/(^|[^\\])"(?:\\.|[^\\"\r\n])*"(?!\s*:)/,lookbehind:!0,greedy:!0},comment:{pattern:/\/\/.*|\/\*[\s\S]*?(?:\*\/|$)/,greedy:!0},number:/-?\b\d+(?:\.\d+)?(?:e[+-]?\d+)?\b/i,punctuation:/[{}[\],]/,operator:/:/,boolean:/\b(?:false|true)\b/,null:{pattern:/\bnull\b/,alias:"keyword"}},e.languages.webmanifest=e.languages.json}e.exports=s,s.displayName="json",s.aliases=["webmanifest"]},21798:(e,s,n)=>{"use strict";var t=n(7110);function a(e){e.register(t),e.languages.jsonp=e.languages.extend("json",{punctuation:/[{}[\]();,.]/}),e.languages.insertBefore("jsonp","punctuation",{function:/(?!\s)[_$a-zA-Z\xA0-\uFFFF](?:(?!\s)[$\w\xA0-\uFFFF])*(?=\s*\()/})}e.exports=a,a.displayName="jsonp",a.aliases=[]},29563:e=>{e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports},65410:(e,s,n)=>{"use strict";var t=n(29563);Object.defineProperty(s,"__esModule",{value:!0}),s.default=void 0,s.default=t(n(21798)).default}}]);