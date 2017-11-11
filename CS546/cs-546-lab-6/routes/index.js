// const postRoutes = require("./posts");
// const userRoutes = require("./users");

const constructorMethod = (app) => {
    
    app.get('/', function (req, res) {
        res.send('This is the main page<br />'+
        'Go to "<a href="http://localhost:3000/about">http://localhost:3000/about</a>" for about info in json from<br />'+
        'Go to "<a href="http://localhost:3000/story">http://localhost:3000/story</a>" for story info in json from<br />'+
        'Go to "<a href="http://localhost:3000/education">http://localhost:3000/education</a>" for education info in json from<br />');
    })
    
    app.get('/about', function (req, res) {
        res.json(
            {
                "name": "Hanrun Li",
                "biography": "Even a monkey can write code that machine can read, only professional programmer can write code that human can read. I heard this words from a friend and now, it become my Coders Creed. I love succinct coding, which means simple, clean and powerful.\n When I am not at work I always spend time on running and exercise. I am very much a kid in heart, love playing video games, watching movies, cooking and traveling wherever I can. I love meeting new people and learning new things, so feel free to say hello and share wonderful stuff with me.",
                "favoriteShows": ["Rick and Morty", "Younger", "Star Trek: Discovery", "The Young Pope"],
                "hobbies": ["Driving", "Swimming", "Hiking", "Games"]
            }
        )
    })

    app.get('/story', function (req, res) {
        res.json(
            {
            "storyTitle": "A Story of Eating and Traveling Around China",
            "story": "It was before I leave China to American, I was sure that I will miss the food and every thing in China. What I did was make a plan to traveling around and eat as much as possible with my girl friend The first station was Sichuan, Haven of Spicy Food! We had Hotpot, Small noodle, Fire noodle, Ice jelly, Spicy BBQ ...... Zhengzhou was my mother town, we also had alot of food in Zhenhzhou I cannot forfet that experience, actually I canot wait to do it again"
            }
        )
    })

    app.get('/education', function (req, res) {
        res.json(
            [
            {
              "schoolName": "Stevens",
              "degree": "Masters degree of Computer Science",
              "favoriteClass": "Introduction to How to Make Your Life Easier",
              "favoriteMemory": "I cannot forget how I first meet my true love, VSCode. It is light weighted, simple to use and really powerful"
            },
            {
              "schoolName": "SUSTC",
              "degree": "Bachelor Degree of Electrical Engineering",
              "favoriteClass": "How Choosing a Major You Donot Like Will Ruin Your Life",
              "favoriteMemory": "I cannot forget the time I spend in the lab doing stuff that I donot like."
            },
            {
            "schoolName": "Huang San Xiao",
            "degree": "Master of Playing with Sands",
            "favoriteClass": "There is nothing more interesting than playing with sands",
            "favoriteMemory": "It was truelly the most easy period of my life, when you are young there was nothing serious that you need to worry about."
            }
            ]
        )
    })
};

module.exports = constructorMethod;

