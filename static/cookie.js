
const cities = 'cities=';

function storeCookie() {
    id = document.getElementById('cityId').innerText;
    currentCookie = cookieValue;
    // if it is empty, initialize
    if (!currentCookie) {
        document.cookie = cities + id ;
    } else {
        // create list
        temp_list = currentCookie.split(',');
        temp_list.push(id);

        // remove duplicates
        city_list = [... new Set(temp_list)];

        // save new cookie as csv
        newCookie = city_list.toString();
        document.cookie = cities + newCookie;
    }
    document.getElementById('city_select').focus();    
}

const cookieValue = document.cookie
  .split("; ")
  .find((row) => row.startsWith(cities))
  ?.split("=")[1];


document.getElementById('addButton').addEventListener('click',storeCookie) 
document.getElementById('city_select').focus();    

if (!document.getElementById('cityId').innerText) {
    document.getElementById('map').hidden = true;
    document.getElementById('temp').hidden = true;
    document.getElementById('windspeed').hidden = true;
} else {
    document.getElementById('map').hidden = false;
    document.getElementById('temp').hidden = false;
    document.getElementById('windspeed').hidden = false;

}

