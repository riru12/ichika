<script lang="ts">
    export let data;
    console.log(data.mangaId);
</script>

<section class="mx-12 md:mx-24 xl:mx-60 2xl:mx-96 py-8">
    <form action={`http://localhost:3000/api/manga/${data.mangaId}/new-chapter?_method=PUT`} method="post" id="new-manga" enctype='multipart/form-data'>
        <div class="flex flex-col gap-4">
            <div class="flex flex-row gap-4 w-full flex-wrap">
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="chapterNo" class="text-sm ml-2">Chapter No.</label>
                    <input type="text" id="chapterNo" name="chapterNo" placeholder="1" class="rounded-3xl px-4 py-1 bg-[#13131a] text-white placeholder:text-neutral-600 ">
                </div>
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="language" class="text-sm ml-2">Language</label>
                    <input type="text" id="language" name="language" placeholder="EN" class="rounded-3xl px-4 py-1 bg-[#13131a] text-white placeholder:text-neutral-600 ">
                </div>
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="title" class="text-sm ml-2">Title</label>
                    <input type="text" id="title" name="title" placeholder="Oneshot" class="rounded-3xl px-4 py-1 bg-[#13131a] text-white placeholder:text-neutral-600 ">
                </div>
            </div>    
            <div>
                <label class="ml-2 text-sm" for="pages">Upload pages:</label> 
                <div class="flex flex-row items-center gap-2 justify-between">
                    <div>
                        <p class="text-xs ml-2 text-red-500"><span class="font-bold">Note:</span> Ensure that the filenames correspond to their page numbers (e.g. <span class="font-mono">1.png</span>, <span class="font-mono">2.png</span>, etc.)</p>
                    </div>
                    <input type="file" multiple id="pages" name="pages" accept="image/png, image/jpeg" class="file:px-4 file:bg-neutral-400 file:text-black file:rounded-3xl file:cursor-pointer hover:file:brightness-125"/>
                </div>
            </div>
            <div class="flex justify-end">
                <button type="submit" form="new-manga" value="Submit" class="px-4 py-1 bg-indigo-700 text-white rounded-3xl hover:brightness-125">Submit</button>
            </div>
        </div>
    </form>
</section>