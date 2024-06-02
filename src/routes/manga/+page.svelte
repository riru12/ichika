<script>
    import "./manga.css";
    import { CldImage } from 'svelte-cloudinary';

    export let data;
</script>

<section class="relative mx-12 md:mx-24 xl:mx-60 2xl:mx-96 py-8">
    <div class="manga-list">
        {#each data.mangaList.mangas as manga}
            <div class="flex flex-row gap-4">
                <a href={`/manga/${manga._id}`}>
                    <CldImage width="500" height="750" src={`${manga._id}/${manga.coverImg}`} alt={`${manga.title} Cover`} class="rounded"/>
                </a>
                <div>  
                    <h2><a href={`/manga/${manga._id}`}>{manga.title}</a></h2>
                    <h3 class="text-neutral-600">{manga.author}</h3>
                    <p>{manga.desc}</p>
                </div>
            </div>
        {/each}
    </div>
    <div class="fixed right-10 bottom-10">
        <a class="px-4 py-2 bg-[#9696c8d9] text-black rounded-3xl" href="/manga/new">Add New Manga</a>
    </div>
</section>