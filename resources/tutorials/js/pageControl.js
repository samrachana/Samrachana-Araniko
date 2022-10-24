var menuIcon = document.getElementById('menuIcon');
var sideMenu = document.getElementById('sideMenu');
var content = document.getElementById('content');
var pageNo = parseInt(document.getElementById('pageNo').innerHTML);
var next = document.getElementById('next');
var prev = document.getElementById('prev');
var scrnSize = document.getElementById('scrnSize');
var tutorialList = ['Introduction', 'Model and Analyse Beams'];
var menuHidden = true;
var fullScreen = false;

window.onload = () => {
    content.style.height = `${window.innerHeight-93}px`;
    sideMenu.style.height = `${window.innerHeight-83}px`;
    document.getElementById('fson').style.display = 'inline';
    document.getElementById('fsoff').style.display = 'none';
    next.style.top = '83px';
    prev.style.top = '0';
    next.style.right = '5%';
}

scrnSize.addEventListener('click', () => {
    if (fullScreen) {
        document.getElementById('fson').style.display = 'inline';
        document.getElementById('fsoff').style.display = 'none';
        content.style.width = '90%';
        content.style.marginLeft = '5%';
        content.style.top = '83px';
        content.style.height = `${window.innerHeight-93}px`;
        document.getElementById('navbar').style.display = 'flex';
        document.getElementById('footer').style.display = 'block';
        fullScreen = false;
        next.style.top = '83px';
        prev.style.top = '0px';
        next.style.right = '5%';
    } else {
        menuIcon.src = '../assets/menu.png';
        sideMenu.style.opacity = 0;
        sideMenu.style.width = '0px';
        sideMenu.style.transitionDuration = '0s';
        content.style.left = '0px';
        content.style.marginLeft = '5%';
        content.style.width = '90%';
        sideMenu.innerHTML = '';
        menuHidden = true;
        document.getElementById('fson').style.display = 'none';
        document.getElementById('fsoff').style.display = 'inline';
        content.style.width = '100%';
        content.style.marginLeft = '0%';
        content.style.top = '0px';
        content.style.height = `${window.innerHeight}px`;
        document.getElementById('navbar').style.display = 'none';
        document.getElementById('footer').style.display = 'none';
        fullScreen = true;
        next.style.top = prev.style.top = '0';
        prev.style.left = next.style.right = '0';
    }
});

if (pageNo < tutorialList.length) {
    next.innerHTML = `${next.innerHTML} <br> <p style='color:white; font-size:large; text-align:center'>${tutorialList[pageNo]}</p>`;
    next.addEventListener('click', () => {
        window.location.href = `${pageNo+1}.html`
    });
} else {
    next.style.display = 'none';
}

if (pageNo > 1) {
    prev.innerHTML = `${prev.innerHTML} <br> <p style='color:white; font-size:large; text-align:center'>${tutorialList[pageNo-2]}</p>`;
    prev.addEventListener('click', () => {
        window.location.href = `${pageNo-1}.html`
    })
} else {
    prev.style.display = 'none';
}

getMenu = () => {
    var temp = [];
    tutorialList.forEach((x) => { temp.push(`<ol><a href = '../pages/${tutorialList.indexOf(x)+1}.html'>${tutorialList.indexOf(x)+1}. ${x}</a></ol>`) });
    return temp.join('');
};

menuIcon.addEventListener('click', () => {
    if (menuHidden) {
        menuIcon.src = '../assets/close.png'
        sideMenu.style.opacity = 0.9;
        sideMenu.style.width = '250px';
        sideMenu.style.transitionDuration = '1s';
        content.style.left = '250px';
        content.style.marginLeft = '0px';
        content.style.width = `${window.innerWidth-250}px`;
        setTimeout(() => { sideMenu.innerHTML = getMenu(); }, 900);
        menuHidden = false;
    } else {
        menuIcon.src = '../assets/menu.png'
        sideMenu.style.opacity = 0;
        sideMenu.style.width = '0px';
        sideMenu.style.transitionDuration = '0s';
        content.style.left = '0px';
        content.style.marginLeft = '5%';
        content.style.width = '90%';
        sideMenu.innerHTML = '';
        menuHidden = true;
    }
});