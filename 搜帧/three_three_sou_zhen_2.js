// 使用第三方库的md5
const CryptoJS = require("crypto-js")

function getXSignature(data) {
    return CryptoJS.MD5(data).toString()
}


var data = '_platform=web,_ts=1729602460221,_versioin=0.2.5,keyword=火车呼啸而过,limit=12,page=16,';
console.log(getXSignature(data));