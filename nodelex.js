class lexi {
    constructor(words) {
        this.words = words;
        this.keywords = ['for', 'else', 'if', 'in', 'range']
        this.mapper = { 'identifiers': [], 'operators': [] }
    }
    findId() {
        var i, j;
        for (i = 0; i < this.words.length; i++) {
            for (j = 0; j < this.words[i].length; j++) {
                //console.log(this.words[i]);
                if (this.words[i][j] == '=') {
                    var c = this.words[i].slice(0, j);


                } else if (this.words[i][j] == "(") {
                    if (this.words[i].slice(0, j) in this.keywords) {


                    }

                }
            }
        }

    }

}
var fs = require('fs')

var globdata = fs.readFileSync("tesy.py", "utf-8");

globdata = globdata.split("\n")
var splitwords = []
var i, j;
for (i = 0; i < globdata.length; i++) {
    for (j of globdata[i].split(" ")) {
        splitwords.push(j);
    }
}
console.log(splitwords);
var lex = new lexi(splitwords);
lex.findId();