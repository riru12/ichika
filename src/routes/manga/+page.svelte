<script>
    import "./manga.css";
    import { CldImage } from 'svelte-cloudinary';

    // obtain manga list from cloudinary (./+page.ts)
    export let data;
</script>

<section class="mx-12 md:mx-24 xl:mx-60 2xl:mx-96 py-8">
    <div class="manga-list">
        {#each data.mangaList as manga}
            <div class="flex flex-row gap-4">
                <a href={`/manga/${manga.path}`}>
                    <CldImage width="500" height="750" src={`${manga.path}/cover`} alt="<Alt Text>" />
                </a>
                <div>
                    <h2><a href={`/manga/${manga.path}`}>{manga.name}</a></h2>
                    <h3>author</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
            </div>
        {/each}
    </div>
</section>