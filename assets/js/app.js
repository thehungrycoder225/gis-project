const api_url = "/api/locator/";

async function getLocation() {
  const myMap = L.map("mapid").setView([13.4157905, 121.9505678], 13);
  const marker = L.marker([0, 0]).addTo(myMap);

  const tileUrl =
    "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}";

  L.tileLayer(tileUrl, {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1,
    accessToken:
      "pk.eyJ1IjoidGhlaHVuZ3J5Y29kZXIiLCJhIjoiY2tmZXg5cXptMDlmcTMxcXYzamhqbm1hOSJ9.X7KQ2n_1P8-zhNVP0ATPZQ",
  }).addTo(myMap);

  const response = await fetch(api_url);
  const data = await response.json();
  for (const i of data) {
    L.marker([i.hlat, i.hlong]).addTo(myMap).bindPopup(
      `"ID":${i.stud_id}<br>
    "Municipality":${i.municipality}<br>
    "Barangay":${i.barangay}<br>
    "Name":${i.stud_name}<br>
    "Age":${i.stud_age}<br>
    "Phone Number":${i.stud_pnumber}<br>
    "Course":${i.stud_course}<br>
    "Year":${i.stud_year}<br>
    "Latitude":${i.hlat}<br>
    "Longtitude":${i.hlong}<br>`
    );
  }
}

getLocation();
