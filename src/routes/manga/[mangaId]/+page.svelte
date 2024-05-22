<script>
    // obtain chapter list for mangaId from cloudinary (./+page.ts)
    export let data;
    console.log(data.mangaId)
</script>


<section>
    {data.mangaId}
    {#each data.chapters as chapter}
        <p>{chapter.name}</p>
    {/each}
</section>