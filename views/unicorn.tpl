<!doctype html>

<html>

%include('head.tpl')
    
<body>
    <section class="unicorn-box">
        <header>
            <img src="/static/images/angry_unicorn.png">
            <h1>Unicornfinder</h1>
        </header>
        
        <article id="unicorn">
            <h2>{{unicorn.get('name')}}</span></h2>
            <div id="unicorn-wrapper">
                
                <div id = "description">
                    <h3>Beskrivning</h3>
                    
                    <p>{{unicorn.get('description')}}</p>
                    
                    <div id="spotted">
                        <p>
                        Enhörningen skådades i {{unicorn.get('spottedWhere', {}).get('name')}} 
                        av {{unicorn.get('reportedBy')}} 
                        {{unicorn.get('spottedWhen', {}).get('date')}}  
                        </p>
                    </div>
                    
                </div>
                
                <div id="unicorn-image">
                    <img class="displayed" src="{{unicorn.get('image')}}">
                </div>
                
            </div>
        </article>
        
    </section>
    <section>
        <article id="lodges">
            <h2>Hotell <span>inom radien av {{radius}}</span></h2>
            %for l in lodgings:
                %if l.get('website') != None:
                <div class="lodge">
                    <a href="{{l.get('website')}}">{{l.get('name')}} {{l.get('rating')}}</a>
                </div>
                %end
            %end
        </article>
    </section>
    
</body>
    
</html>