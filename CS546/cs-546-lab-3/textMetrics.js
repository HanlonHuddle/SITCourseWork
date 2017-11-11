// totalLetters: total number of letters in the simplified text,
// totalWords: total number of words in the simplified text; numbers count as words,
// uniqueWords: total number of unique words that appear in the simplified text; numbers count as words,
// longWords: number of words in the text that are 6 or more letters long; this is a total count of distinct words, not unique words; numbers count as words,
// averageWordLength: the average number of letters in a word in the text; numbers count as words,
// wordOccurrences: a dictionary of each word and how many times each word occurs in the text; numbers count as words

module.exports = {
    simplify: function(text){
        if (!text) throw "You must provide a text";
        if (typeof text !== "string") throw "You must provide a string as text";
        // to lowercase
        lText = text.toLowerCase();
        // replace all non-alphanumeric with ' ' white space
        lText = lText.replace(/\s\s+/g, ' ');
        lText = lText.replace(/\n/g, ' ');
        lText = lText.replace(/\t/g, ' ');
        // return and also trim the string with leading&ending spaces
        lText = lText.replace(/[^a-zA-Z0-9\s]/g, '');
        // replace spaces with single simple space
        return lText.trim();
    },
    createMetrics: function(text){
        if (!text) throw "You must provide a text";
        if (typeof text !== "string") throw "You must provide a string as text";
        sText = this.simplify(text);
        // only count lowercase letters since text is simplified (according to the example result provided by the assignment, the space should also be counted)
        var rx = /[a-z0-9\s]/gi;
        var totalLetters = sText.match(rx).length;
        // split and count words
        var wordsArray = sText.split(' ');
        var totalWords = wordsArray.length;
        // fake hash
        var wordOccurrences = {};
        var longWords = 0;
        var totalLengthOfWrods = 0;
        for (word of wordsArray) {
            totalLengthOfWrods += word.length;
            if (word.length >= 6)
                longWords += 1;
            if (word in wordOccurrences)
                wordOccurrences[word] += 1;
            else{
                wordOccurrences[word] = 1;
            }
        }
        var uniqueWords = Object.keys(wordOccurrences).length;
        var averageWordLength = totalLengthOfWrods / totalWords;
        // wordOccurrences = Object.keys(wordOccurrences).sort(function(a,b){return wordOccurrences[a]-wordOccurrences[b]});
        return ({totalLetters: totalLetters,
            totalWords: totalWords,
            uniqueWords: uniqueWords,
            longWords: longWords,
            averageWordLength: averageWordLength,
            wordOccurrences: wordOccurrences
            });
    }
}