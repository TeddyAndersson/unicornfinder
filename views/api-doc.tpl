<!doctype html>

<html>

%include('head.tpl')
    
<body>
    <section id="section-api">
        <article class="api-doc">
                <h1 class="title">API - Beskrivning</h1>
                <p>I listan nedan kan en specifik enhörning nås med hjälp av ett id-nummer. Det är alltid ett heltal, men skrivs nedan som {id}. Ersätt därför hela {id} med id-numret på den enhörning du vill nå.

Exemplen är beskrivna med JSON. XML-varianten är likartade. Det förvalda utmatningformatet är HTML. För att få ut JSON ska HTTP-headern Accept: application/json skickas. För att få ut XML används Accept: application/xml. API:t accepterar indata som både JSON och XML.</p>
        </article>
        
        <article class="api-doc">
            <h2 class="title">GET /unicorns</h2>
            <p>Hämta en lista över alla enhörningar. Listan innehåller enhörningens namn, id och en länk till vidare beskrivning.</p>
            <h3 class="subtitle">Indata</h3>
            <p>Indata är ej möjligt för get metoden</p>
            <h3 class="subtitle">Returdata</h3>
            <pre>
                <code>
[
  {
    "id": "1",
    "name": "Nordsvensk travhörning",
    "details": "http://unicorns.idioti.se/1"
  },
  {
    "id": "2",
    "name": "Karibisk strandponny",
    "details": "http://unicorns.idioti.se/2"
  }
]
                </code>
            </pre>
        </article>
        
        <article class="api-doc">
            <h2 class="title">GET /unicorn/{id}</h2>
             <p>Hämtar ut information om en specefik enhörning och de hotell som finns i närheten samt vilken radie hotellen befinner sig i.</p>
            <h3 class="subtitle">Indata</h3>
            <p>Indata är ej möjligt för get metoden</p>
            <h3 class="subtitle">Returdata</h3>
            <pre>
                <code>
{
  "nearbyLodgings": {
    "lodgings": [
      {
        "website": "http://www.admiralhotel.dk/",
        "rating": 4,
        "name": "Copenhagen Admiral Hotel"
      },
      {
        "website": "http://www.marriott.com/hotels/travel/cphdk-copenhagen-marriott-hotel/",
        "rating": 3.7,
        "name": "Copenhagen Marriott Hotel"
      },
      {
        "website": "http://www.radissonblu.com/royalhotel-copenhagen",
        "rating": 4,
        "name": "Radisson Blu Royal Hotel,Copenhagen"
      }
    ],
    "lodgingSearchRadius": "7000"
  },
  "description": "Den här enhörningen var en av mina första. Jag hittade den på Zoo i Köpenhamn när jag gick på mellanstadiet. Den indiska            enhörningen är lite rundare i formerna än vad enhörningar vanligen är. Notera även den gråa huden och den nästan totala avsaknaden av hår. Min    granne Ravi hävdar envist att det är en indisk noshörning, men det tror jag inte ett dugg på.",
  "reportedBy": "Johan",
  "image": "http://unicorns.idioti.se/bilder/indisk.jpg",
  "spottedWhen": {
    "date": "1994-05-20",
    "timezone_type": 3,
    "timezone": "UTC"
  },
  "spottedWhere": {
    "lat": "55.671",
    "lon": "12.5212",
    "name": "Köpenhamn, Danmark"
  },
  "id": "5",
  "name": "Indisk enhörning"
}
                </code>
            </pre>
        </article>
        
    </section>
    
</body>
    
</html>
 