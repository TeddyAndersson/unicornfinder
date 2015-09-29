<!doctype html>

<html>

%include('head.tpl')
    
<body>
    <section>
        <header>
            <img src="/static/images/angry_unicorn.png">
            <h1>Unicornfinder</h1>
        </header>
        %for u in unicorn_list:
        <article>
            <a href="/unicorn/{{u.get('id')}}">{{u.get('name')}} <span class="link_arrow">&#8227;</span></a>
        </article>
        %end
        
    </section>
    
</body>
    
</html>
 