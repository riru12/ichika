<script>
    import "./manga.css";
    import { CldImage } from 'svelte-cloudinary';

    export let data;
</script>

<section class="relative mx-12 md:mx-24 xl:mx-60 2xl:mx-96 py-8">
    <div class="manga-list">
        {#each data.mangaList.mangas as manga}
            <div class="flex flex-row gap-4">
                <a href={`/manga/${manga._id}`} class="max-h-48">
                    <CldImage width="500" height="750" src={`${manga._id}/${manga.coverImg}`} alt={`${manga.title} Cover`} class="rounded"/>
                </a>
                <div>  
                    <h2><a href={`/manga/${manga._id}`}>{manga.title}</a></h2>
                    <h3 class="text-neutral-600">{manga.author}</h3>
                    <p>{manga.desc}</p>
                    <div class="flex flex-row gap-2 mt-4 flex-wrap">
                        {#each manga.genres as genre}
                            <div class="text-sm bg-neutral-800 px-3 py-1 rounded-xl">{genre}</div>
                        {/each}
                    </div>
                </div>
            </div>
        {/each}
    </div>
    <div class="fixed right-10 bottom-10">
        <a class="px-4 py-2 bg-indigo-700 flex flex-row justify-center items-center gap-3 text-white hover:brightness-125 rounded-[50%] h-12 w-12 md:h-auto md:w-auto md:rounded-3xl" href="/manga/new">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="size-4">
                <path d="M8.75 3.75a.75.75 0 0 0-1.5 0v3.5h-3.5a.75.75 0 0 0 0 1.5h3.5v3.5a.75.75 0 0 0 1.5 0v-3.5h3.5a.75.75 0 0 0 0-1.5h-3.5v-3.5Z" />
            </svg>
            <span class="hidden md:block">Add New Manga</span>
        </a>
    </div>
</section>