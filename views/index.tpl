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
            <img sr="">
            <h2>{{u.get("name")}}</h2>
            <p>
                
            </p>
        </article>
        %end
        
    </section>
    
</body>
    
</html>
 