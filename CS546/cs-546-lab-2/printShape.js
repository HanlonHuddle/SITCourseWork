module.exports = {
    triangle: function(lines) {
        if (arguments.length !== 1)
            throw("Please input one integer as the input for this function");
        if (typeof lines !== "number" || lines !== parseInt(lines, 10) || lines <= 0)
            throw("The integer must be larger than 1");
        

        for (var i = 1; i <= lines; i++) {
            var str = "";
            for (j = 1; j <= lines - i; j++) {
                str += " ";
            }
            str += "/";
            if (i !== lines)
                for (j = 1; j < i; j++) {
                    str += "  ";
                }
            else
                for (j = 1; j < i; j++) {
                    str += "--";
                }
                
            str += "\\";
            console.log(str);
        }
    },

    square: function(lines) {
        if (arguments.length !== 1)
            throw("Please input one integer as the input for this function");
        if (typeof lines !== "number" || lines !== parseInt(lines, 10) || lines <= 1)
            throw("The integer must be larger than 1");

        for (var i = 1; i <= lines; i++) {
            var str = "|";
            if (i == 1 || i == lines) {
                for (j = 1; j<=lines; j++)
                    str += "-";
            }
            else {
                for (j = 1; j<=lines; j++)
                    str += " ";
            }
            str+="|";
            console.log(str);
        }
    },

    rhombus: function(lines) {
        if (arguments.length !== 1)
            throw("Please input one integer as the input for this function");
        if (typeof lines !== "number" || lines !== parseInt(lines, 10) || lines <= 1 || lines % 2 !== 0)
            throw("Please input one even integer (larger than 1) as the input for this function");

        h = lines / 2;
        str = "";
        
        for (i=1; i<=h; i++) {
            str = "";
            for (j = 1; j <= h - i; j++) {
                str+=" ";
            }
            if (i == 1)
                str+="/-";
            else
                str+="/ ";
            for (j = 1; j<i; j++) {
                str+="  ";
            }
            str+="\\";
            console.log(str);
        }

        for (i=1; i<=h; i++) {
            str = "";
            for (j = 1; j < i; j++) {
                str+=" ";
            }
            if (i == h)
                str+="\\-";
            else
                str+="\\ ";
            for (j = 1; j <= h-i; j++) {
                str+="  ";
            }
            str+="/";
            console.log(str);
        }

    }
};