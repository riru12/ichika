<script>
    export let data;
    console.log(data.chapters);
</script>

<h1>{data.slug}</h1>

<section>
    {#each data.chapters as chapters}
        <a href={`/reader/${chapters.path}`}><div>{chapters.name}</div></a>
    {/each}
</section>