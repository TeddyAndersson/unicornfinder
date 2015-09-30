<!doctype html>

<html>

%include('head.tpl')
    
<body>
    <section>
        <header>
            <img src="/static/images/angry_unicorn.png">
            <h1>Unicornfinder</h1>
        </header>
        
        <article>
            <a href="/unicorn/{{u.get('id')}}">{{unicorn.get('name')}} <span class="link_arrow">&#8227;</span></a>
        </article>
        
    </section>
    
</body>
    
</html>