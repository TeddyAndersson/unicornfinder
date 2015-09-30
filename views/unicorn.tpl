<!doctype html>

<html>

%include('head.tpl')
    
<body>
    <section>
        <header>
            <img src="/static/images/angry_unicorn.png">
            <h1>Unicornfinder</h1>
        </header>
        
        <article class="unicorn">
            <h2>{{unicorn.get('name')}}</span></h2>
            <div class = "description">
                <h3>Beskrivning av enhörningen</h3>
                <p>{{unicorn.get('description')}}</p>
            </div>
            <img src="{{unicorn.get('image')}}">
            <div class ="reportedby">
                <p>Enhörning har skådats av: {{unicorn.get('reportedby')}}</p>
            </div>
            <p>d</p>
        </article>
        
    </section>
    
</body>
    
</html>