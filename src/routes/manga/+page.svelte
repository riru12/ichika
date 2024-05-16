<script lang="ts">
    import "./manga.css";

    import { CldImage } from 'svelte-cloudinary';

    let folders: any = [];
    let data: any = {};
    async function fetchRootFolders(){
        const response = await fetch(`http://localhost:3000/root_folders`);
        data = await response.json();
        folders = data.folders;

        console.log(folders);
    }
    fetchRootFolders();

</script>

<section class="mx-12 md:mx-24 xl:mx-60 2xl:mx-96 py-8">
    <div class="manga-list">
        {#each folders as manga}
            <div class="flex flex-row">
                <a href={`/manga/${manga.path}`}>
                    <CldImage width="500" height="750" src={`${manga.path}/cover`} alt="<Alt Text>" />
                </a>
                <div>
                    {manga.path}
                </div>
            </div>
        {/each}
    </div>
</section>