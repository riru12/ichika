<script>
    // obtain chapter list for mangaId from cloudinary (./+page.ts)
    export let data;
</script>


<section>
    {#each data.chapters as chapter}
        <p>{chapter.name}</p>
    {/each}
</section>