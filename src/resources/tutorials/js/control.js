var menuIcon = document.getElementById('menuIcon');
var sideMenu = document.getElementById('sideMenu');
var search = document.getElementById('search');
var searchBox = document.getElementById('searchBox');
var searchResults = document.getElementById('searchResults');

var tutorialList = ['Introduction', 'Model and Analyse Beams'];
var keywords = [
    ['introduction', 'interface', 'basic', 'drawing', 'modelling', 'segment', 'support', 'load', 'file', 'save', 'open', 'edit'],
    ['beams', 'simple', 'supported', 'analyse', 'diagram']
];
var menuHidden = true;
var found = '';

getMenu = () => {
    var temp = [];
    tutorialList.forEach((x) => { temp.push(`<ol><a href = 'pages/${tutorialList.indexOf(x)+1}.html'>${tutorialList.indexOf(x)+1}. ${x}</a></ol>`) });
    return temp.join('');
};

matchWords = (a, b) => {
    let target = a.length < b.length ? a : b;
    let aim = target == a ? b : a;
    let score = 0;
    let index = target.length;
    while (score == 0 && index != 0) {
        if (aim.search(target.slice(0, index)) != -1) {
            score = Math.floor(100 * index / target.length);
        }
        index = index - 1;
    }
    return score
};

matchWordInList = (word, listOfWords) => {
    let score = 0;
    for (x of listOfWords) {
        let temp = matchWords(word.toLowerCase(), x.toLowerCase());
        if (temp > score) {
            score = temp;
        }
    }
    return score;
}

matchListInList = (l1, l2) => {
    let score = 0;
    for (x of l1) {
        let temp = matchWordInList(x, l2);
        if (temp > score) {
            score = temp;
        }
    }
    return score;
}

searchByKeywords = (toSearch) => {
    toSearch = toSearch.toLowerCase();
    let allWords = toSearch.split(' ');
    let words = [];
    allWords.forEach((x) => {
        if (x.length > 3) {
            words.push(x)
        }
    })
    let results = [];
    keywords.forEach((kw) => { results.push([keywords.indexOf(kw) + 1, matchListInList(words, kw)]) });
    results.sort((a, b) => { return b[1] - a[1] });
    return results;
};

menuIcon.addEventListener('click', () => {
    if (menuHidden) {
        menuIcon.src = 'assets/close.png';
        sideMenu.style.opacity = 0.9;
        sideMenu.style.width = '250px';
        sideMenu.style.transitionDuration = '1s';
        search.style.left = '250px';
        setTimeout(() => { sideMenu.innerHTML = getMenu(); }, 900);
        menuHidden = false;
    } else {
        menuIcon.src = 'assets/menu.png';
        sideMenu.style.opacity = 0;
        sideMenu.style.width = '0px';
        sideMenu.style.transitionDuration = '0s';
        search.style.left = '0px';
        sideMenu.innerHTML = '';
        menuHidden = true;
    }
});
setInterval(() => {
    if (searchBox.value.length > 0) {
        if (searchBox.value != found) {
            searchResults.innerHTML = "<p style='padding:10px; font-size:20px; color:white'>These tutorials may help you the best...</p>"
            searchResults.style.opacity = 1;
            let displayResults = [];
            searchByKeywords(searchBox.value).forEach((x) => {
                displayResults.push(`<ol><a href = 'pages/${x[0]}.html'>#${x[0]} ${tutorialList[x[0]-1]} ${x[1]>80?'&#9733 &#9733 &#9733':(x[1]>50?'&#9733 &#9733':(x[1]>25?'&#9733':'&#10008'))}</a></ol>`);
            })
            searchResults.innerHTML = searchResults.innerHTML + displayResults.join('');
            found = searchBox.value;
        }
    } else {
        searchResults.style.opacity = 0;
        searchResults.innerHTML = '';
        found = '';
    };
}, 500);