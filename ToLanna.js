var fs = require('fs');

var j = fs.readFileSync("words.json").toString();
var json = JSON.parse(j);

function ToLanna(content){
    lanna = content;
    //ME
    Object.keys(json.me).forEach(function(e){
        lanna = lanna.replace(e,json.me[e]);
    });

    //YOU
    Object.keys(json.you).forEach(function(e){
        lanna = lanna.replace(e,json.you[e]);
    });

    //TIMES
    Object.keys(json.times).forEach(function(e){
        lanna = lanna.replace(e,json.times[e]);
    });

    //OTHERS
    Object.keys(json.others).forEach(function(e){
        lanna = lanna.replace(e,json.others[e]);
    });

    //FAMILY
    Object.keys(json.family).forEach(function(e){
        lanna = lanna.replace(e,json.family[e]);
    });

    //NUMBERS
    Object.keys(json.numbers).forEach(function(e){
        lanna = lanna.replace(e,json.numbers[e]);
    });
    return lanna;
}
