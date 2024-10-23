// 使用第三方库的md5，生成kg_mid

const CryptoJS = require("crypto-js")

function GetMid() {
    function Guid() {
        function e() {
            return (65536 * (1 + Math.random()) | 0).toString(16).substring(1)
        }
        return e() + e() + "-" + e() + "-" + e() + "-" + e() + "-" + e() + e() + e()
    }

    return CryptoJS.MD5(Guid()).toString()
}

// =============================================================================

// u.signature = v.signatureParam(u, '1014');
// dfid: signature参数，使用第三方MD5。(注意：如果MD5算法被魔改，需要扣代码，而不是直接使用第三方库)
function signatureParam(e, t) {
    var n = new Array;
    for (var i in e)
        e.hasOwnProperty(i) && "signature" != i && n.push(e[i]);
    for (var r = n.sort(), a = "", o = 0, s = r.length; o < s; o++)
        a += r[o];
    return CryptoJS.MD5(t + a + t).toString()
}

// =============================================================================
// dfid: data参数
function getFormData(dt, time, mid) {
    var e = {
        "appCodeName": "Mozilla",
        "appName": "Netscape",
        "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "connection": "other",
        "doNotTrack": "1",
        "hardwareConcurrency": 16,
        "language": "zh-CN",
        "languages": "zh-CN,zh,en",
        "maxTouchPoints": 0,
        "mimeTypes": "application/pdf,text/pdf",
        "platform": "Win32",
        "plugins": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "colorDepth": 24,
        "pixelDepth": 24,
        "screenResolution": "1536x864",
        "timezoneOffset": -480,
        "sessionStorage": true,
        "localStorage": true,
        "indexedDB": true,
        "cookie": true,
        "adBlock": false,
        "devicePixelRatio": 1.25,
        "hasLiedOs": false,
        "hasLiedLanguages": false,
        "hasLiedResolution": false,
        "hasLiedBrowser": false,
        "webglRenderer": "ANGLE (AMD, AMD Radeon(TM) Graphics (0x00001636) Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "webglVendor": "Google Inc. (AMD)",
        "canvas": "1b5c1bba0d39c2d6db2a2b40fbd360f2",
        "fonts": "Arial,Arial Black,Arial Narrow,Arial Unicode MS,Book Antiqua,Bookman Old Style,Calibri,Cambria,Cambria Math,Century,Century Gothic,Century Schoolbook,Comic Sans MS,Consolas,Courier,Courier New,Georgia,Helvetica,Impact,Lucida Bright,Lucida Calligraphy,Lucida Console,Lucida Fax,Lucida Handwriting,Lucida Sans,Lucida Sans Typewriter,Lucida Sans Unicode,Microsoft Sans Serif,Monotype Corsiva,MS Gothic,MS PGothic,MS Reference Sans Serif,MS Sans Serif,MS Serif,Palatino Linotype,Segoe Print,Segoe Script,Segoe UI,Segoe UI Light,Segoe UI Semibold,Segoe UI Symbol,Tahoma,Times,Times New Roman,Trebuchet MS,Verdana,Wingdings,Wingdings 2,Wingdings 3,Agency FB,Algerian,Baskerville Old Face,Bauhaus 93,Bell MT,Berlin Sans FB,Bernard MT Condensed,Blackadder ITC,Bodoni MT,Bodoni MT Black,Bodoni MT Condensed,Bookshelf Symbol 7,Bradley Hand ITC,Broadway,Brush Script MT,Californian FB,Calisto MT,Candara,Castellar,Centaur,Chiller,Colonna MT,Constantia,Cooper Black,Copperplate Gothic,Copperplate Gothic Light,Corbel,Curlz MT,DFKai-SB,Ebrima,Edwardian Script ITC,Elephant,Engravers MT,FangSong,Felix Titling,Footlight MT Light,Forte,Freestyle Script,French Script MT,Gabriola,Gigi,Gill Sans MT,Gill Sans MT Condensed,Goudy Old Style,Goudy Stout,Haettenschweiler,Harrington,High Tower Text,Imprint MT Shadow,Informal Roman,Jokerman,Juice ITC,KaiTi,Kristen ITC,Kunstler Script,Leelawadee,Magneto,Maiandra GD,Malgun Gothic,Marlett,Matura MT Script Capitals,Meiryo,Meiryo UI,Microsoft Himalaya,Microsoft JhengHei,Microsoft New Tai Lue,Microsoft PhagsPa,Microsoft Tai Le,Microsoft Uighur,Microsoft YaHei,Microsoft Yi Baiti,MingLiU,MingLiU_HKSCS,MingLiU_HKSCS-ExtB,MingLiU-ExtB,Mistral,Modern No. 20,Mongolian Baiti,MS Reference Specialty,MS UI Gothic,MT Extra,MV Boli,Niagara Engraved,Niagara Solid,NSimSun,Old English Text MT,Onyx,Palace Script MT,Papyrus,Parchment,Perpetua,Perpetua Titling MT,Playbill,PMingLiU,PMingLiU-ExtB,Poor Richard,Pristina,Ravie,Rockwell,Rockwell Condensed,Showcard Gothic,SimHei,SimSun,SimSun-ExtB,Snap ITC,Stencil,Sylfaen,Tempus Sans ITC,Tw Cen MT,Tw Cen MT Condensed,Viner Hand ITC,Vivaldi,Vladimir Script,Wide Latin",
        "dt": dt, // ?
        "time": time, // ?
        "userid": "",
        "mid": mid, // ?
        "uuid": "1b3b62c4c25a2a74c07c91edb73e2b0e",
        "appid": "1014",
        "webdriver": false,
        "callPhantom": false,
        "tempKgMid": mid, // ?
        "referrer": "https://www.kugou.com/yy/html/search.html",
        "source": "https://www.kugou.com/mixsong/gr4tu0a.html?fromsearch=%E9%82%93%E7%B4%AB%E6%A3%8B",
        "clientAppid": "",
        "clientver": "",
        "clientMid": "",
        "clientDfid": "",
        "clientUserId": "",
        "audioKey": "124.04347527516074"
    }

    t = JSON.stringify(e)
    var l = CryptoJS.enc.Utf8.parse(t);
    return CryptoJS.enc.Base64.stringify(l)
}

// =============================================================================

// 'encode_album_audio_id' : '10qgrdcc', # ?
// 生成 请求里的signature参数

function calcMD5(t, r) {
    var t = t.join("")
        // u = m(u = m(u = m(u = m(u = h(u = h(u = h(u = h(u = p(u = p(u = p(u = p(u = b(u = b(u = b(u = b(u, f = b(f, d = b(d, l = b(l, u, f, d, s[g + 0], 7, -680876936), u, f, s[g + 1], 12, -389564586), l, u, s[g + 2], 17, 606105819), d, l, s[g + 3], 22, -1044525330), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 4], 7, -176418897), u, f, s[g + 5], 12, 1200080426), l, u, s[g + 6], 17, -1473231341), d, l, s[g + 7], 22, -45705983), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 8], 7, 1770035416), u, f, s[g + 9], 12, -1958414417), l, u, s[g + 10], 17, -42063), d, l, s[g + 11], 22, -1990404162), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 12], 7, 1804603682), u, f, s[g + 13], 12, -40341101), l, u, s[g + 14], 17, -1502002290), d, l, s[g + 15], 22, 1236535329), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 1], 5, -165796510), u, f, s[g + 6], 9, -1069501632), l, u, s[g + 11], 14, 643717713), d, l, s[g + 0], 20, -373897302), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 5], 5, -701558691), u, f, s[g + 10], 9, 38016083), l, u, s[g + 15], 14, -660478335), d, l, s[g + 4], 20, -405537848), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 9], 5, 568446438), u, f, s[g + 14], 9, -1019803690), l, u, s[g + 3], 14, -187363961), d, l, s[g + 8], 20, 1163531501), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 13], 5, -1444681467), u, f, s[g + 2], 9, -51403784), l, u, s[g + 7], 14, 1735328473), d, l, s[g + 12], 20, -1926607734), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 5], 4, -378558), u, f, s[g + 8], 11, -2022574463), l, u, s[g + 11], 16, 1839030562), d, l, s[g + 14], 23, -35309556), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 1], 4, -1530992060), u, f, s[g + 4], 11, 1272893353), l, u, s[g + 7], 16, -155497632), d, l, s[g + 10], 23, -1094730640), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 13], 4, 681279174), u, f, s[g + 0], 11, -358537222), l, u, s[g + 3], 16, -722521979), d, l, s[g + 6], 23, 76029189), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 9], 4, -640364487), u, f, s[g + 12], 11, -421815835), l, u, s[g + 15], 16, 530742520), d, l, s[g + 2], 23, -995338651), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 0], 6, -198630844), u, f, s[g + 7], 10, 1126891415), l, u, s[g + 14], 15, -1416354905), d, l, s[g + 5], 21, -57434055), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 12], 6, 1700485571), u, f, s[g + 3], 10, -1894986606), l, u, s[g + 10], 15, -1051523), d, l, s[g + 1], 21, -2054922799), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 8], 6, 1873313359), u, f, s[g + 15], 10, -30611744), l, u, s[g + 6], 15, -1560198380), d, l, s[g + 13], 21, 1309151649), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 4], 6, -145523070), u, f, s[g + 11], 10, -1120210379), l, u, s[g + 2], 15, 718787259), d, l, s[g + 9], 21, -343485551),
        // 里面的 m，h, p, b函数
        // b = _ff, p = _gg, h = _hh, m = _ii
    function _ff(t, n, r, e, o, i, c) {
        var s = t + (n & r | ~n & e) + (o >>> 0) + c;
        return (s << i | s >>> 32 - i) + n
    }

    function _gg(t, n, r, e, o, i, c) {
        var s = t + (n & e | r & ~e) + (o >>> 0) + c;
        return (s << i | s >>> 32 - i) + n
    }

    function _hh(t, n, r, e, o, i, c) {
        var s = t + (n ^ r ^ e) + (o >>> 0) + c;
        return (s << i | s >>> 32 - i) + n
    }

    function _ii(t, n, r, e, o, i, c) {
        var s = t + (r ^ (n | ~e)) + (o >>> 0) + c;
        return (s << i | s >>> 32 - i) + n
    }

    // ===========================================================================
    // t.constructor == String ? t = c && "binary" === c.encoding ? o.stringToBytes(t) : r.stringToBytes(t) : e(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
    // 里面的 r.stringToBytes
    var r2 = {
        utf8: {
            stringToBytes: function(t) {
                return r2.bin.stringToBytes(unescape(encodeURIComponent(t)))
            },
            bytesToString: function(t) {
                return decodeURIComponent(escape(r2.bin.bytesToString(t)))
            }
        },
        bin: {
            stringToBytes: function(t) {
                for (var n = [], r = 0; r < t.length; r++)
                    n.push(255 & t.charCodeAt(r));
                return n
            },
            bytesToString: function(t) {
                for (var n = [], r = 0; r < t.length; r++)
                    n.push(String.fromCharCode(t[r]));
                return n.join("")
            }
        }
    }

    // ===========================================================================
    // var e = n.wordsToBytes(i(t, r)); 代码里的 n.wordsToBytes
    var n2 = {
        n: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
        r: {
            rotl: function(t, n) {
                return t << n | t >>> 32 - n
            },
            rotr: function(t, n) {
                return t << 32 - n | t >>> n
            },
            endian: function(t) {
                if (t.constructor == Number)
                    return 16711935 & n2.r.rotl(t, 8) | 4278255360 & n2.r.rotl(t, 24);
                for (var n = 0; n < t.length; n++)
                    t[n] = n2.r.endian(t[n]);
                return t
            },
            randomBytes: function(t) {
                for (var n = []; t > 0; t--)
                    n.push(Math.floor(256 * Math.random()));
                return n
            },
            bytesToWords: function(t) {
                for (var n = [], r = 0, e = 0; r < t.length; r++,
                    e += 8)
                    n[e >>> 5] |= t[r] << 24 - e % 32;
                return n
            },
            wordsToBytes: function(t) {
                for (var n = [], r = 0; r < 32 * t.length; r += 8)
                    n.push(t[r >>> 5] >>> 24 - r % 32 & 255);
                return n
            },
            bytesToHex: function(t) {
                for (var n = [], r = 0; r < t.length; r++)
                    n.push((t[r] >>> 4).toString(16)),
                    n.push((15 & t[r]).toString(16));
                return n.join("")
            },
            hexToBytes: function(t) {
                for (var n = [], r = 0; r < t.length; r += 2)
                    n.push(parseInt(t.substr(r, 2), 16));
                return n
            },
            bytesToBase64: function(t) {
                for (var r = [], e = 0; e < t.length; e += 3)
                    for (var o = t[e] << 16 | t[e + 1] << 8 | t[e + 2], i = 0; i < 4; i++)
                        8 * e + 6 * i <= 8 * t.length ? r.push(n.charAt(o >>> 6 * (3 - i) & 63)) : r.push("=");
                return r.join("")
            },
            base64ToBytes: function(t) {
                t = t.replace(/[^A-Z0-9+\/]/gi, "");
                for (var r = [], e = 0, o = 0; e < t.length; o = ++e % 4)
                    0 != o && r.push((n.indexOf(t.charAt(e - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | n.indexOf(t.charAt(e)) >>> 6 - 2 * o);
                return r
            }
        }
        //t.exports = r
    }

    // ===========================================================================

    // var e = n.wordsToBytes(i(t, r)); 代码里的 i
    function i(t, c) {
        t.constructor == String ? t = c && "binary" === c.encoding ? o.stringToBytes(t) : r2.utf8.stringToBytes(t) : e(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
        for (var s = n2.r.bytesToWords(t), a = 8 * t.length, l = 1732584193, u = -271733879, f = -1732584194, d = 271733878, g = 0; g < s.length; g++)
            s[g] = 16711935 & (s[g] << 8 | s[g] >>> 24) | 4278255360 & (s[g] << 24 | s[g] >>> 8);
        s[a >>> 5] |= 128 << a % 32,
            s[14 + (a + 64 >>> 9 << 4)] = a;
        for (var b = _ff, p = _gg, h = _hh, m = _ii, g = 0; g < s.length; g += 16) {
            var y = l,
                j = u,
                S = f,
                v = d;
            u = m(u = m(u = m(u = m(u = h(u = h(u = h(u = h(u = p(u = p(u = p(u = p(u = b(u = b(u = b(u = b(u, f = b(f, d = b(d, l = b(l, u, f, d, s[g + 0], 7, -680876936), u, f, s[g + 1], 12, -389564586), l, u, s[g + 2], 17, 606105819), d, l, s[g + 3], 22, -1044525330), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 4], 7, -176418897), u, f, s[g + 5], 12, 1200080426), l, u, s[g + 6], 17, -1473231341), d, l, s[g + 7], 22, -45705983), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 8], 7, 1770035416), u, f, s[g + 9], 12, -1958414417), l, u, s[g + 10], 17, -42063), d, l, s[g + 11], 22, -1990404162), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 12], 7, 1804603682), u, f, s[g + 13], 12, -40341101), l, u, s[g + 14], 17, -1502002290), d, l, s[g + 15], 22, 1236535329), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 1], 5, -165796510), u, f, s[g + 6], 9, -1069501632), l, u, s[g + 11], 14, 643717713), d, l, s[g + 0], 20, -373897302), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 5], 5, -701558691), u, f, s[g + 10], 9, 38016083), l, u, s[g + 15], 14, -660478335), d, l, s[g + 4], 20, -405537848), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 9], 5, 568446438), u, f, s[g + 14], 9, -1019803690), l, u, s[g + 3], 14, -187363961), d, l, s[g + 8], 20, 1163531501), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 13], 5, -1444681467), u, f, s[g + 2], 9, -51403784), l, u, s[g + 7], 14, 1735328473), d, l, s[g + 12], 20, -1926607734), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 5], 4, -378558), u, f, s[g + 8], 11, -2022574463), l, u, s[g + 11], 16, 1839030562), d, l, s[g + 14], 23, -35309556), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 1], 4, -1530992060), u, f, s[g + 4], 11, 1272893353), l, u, s[g + 7], 16, -155497632), d, l, s[g + 10], 23, -1094730640), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 13], 4, 681279174), u, f, s[g + 0], 11, -358537222), l, u, s[g + 3], 16, -722521979), d, l, s[g + 6], 23, 76029189), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 9], 4, -640364487), u, f, s[g + 12], 11, -421815835), l, u, s[g + 15], 16, 530742520), d, l, s[g + 2], 23, -995338651), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 0], 6, -198630844), u, f, s[g + 7], 10, 1126891415), l, u, s[g + 14], 15, -1416354905), d, l, s[g + 5], 21, -57434055), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 12], 6, 1700485571), u, f, s[g + 3], 10, -1894986606), l, u, s[g + 10], 15, -1051523), d, l, s[g + 1], 21, -2054922799), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 8], 6, 1873313359), u, f, s[g + 15], 10, -30611744), l, u, s[g + 6], 15, -1560198380), d, l, s[g + 13], 21, 1309151649), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 4], 6, -145523070), u, f, s[g + 11], 10, -1120210379), l, u, s[g + 2], 15, 718787259), d, l, s[g + 9], 21, -343485551),
                l = l + y >>> 0,
                u = u + j >>> 0,
                f = f + S >>> 0,
                d = d + v >>> 0
        }
        return n2.r.endian([l, u, f, d])
    }

    if (void 0 === t || null === t)
        throw new Error("Illegal argument " + t);
    var e = n2.r.wordsToBytes(i(t, r));
    return r && r.asBytes ? e : r && r.asString ? o.bytesToString(e) : n2.r.bytesToHex(e)
}

var s = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014",
    "bitrate=0",
    "callback=callback123",
    "clienttime=1729657418208",
    "clientver=1000",
    "dfid=3x6rqf3YCp2w0S2qT14HnBTX",
    "filter=10",
    "inputtype=0",
    "iscorrection=1",
    "isfuzzy=0",
    "keyword=王力宏",
    "mid=94e95cefa9686611ee8df0d86817a2b4",
    "page=1",
    "pagesize=30",
    "platform=WebFilter",
    "privilege_filter=0",
    "srcappid=2919",
    "token=",
    "userid=0",
    "uuid=94e95cefa9686611ee8df0d86817a2b4",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]

// =============================================================================

//console.log(GetMid())
//console.log(signatureParam(u, '1014'))
//console.log(getFormData('2024-10-23', '2024-10-23 09:40:50', GetMid()))
console.log(calcMD5(s))