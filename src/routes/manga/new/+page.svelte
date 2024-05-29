<section class="mx-12 md:mx-24 xl:mx-60 2xl:mx-96 py-8">
    <form action="http://localhost:3000/api/manga/new" method="post" id="new-manga" enctype='multipart/form-data'>
        <div class="flex flex-col gap-4">
            <div class="flex flex-row gap-4 w-full flex-wrap">
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="title" class="text-sm ml-2">Title</label>
                    <input type="text" id="title" name="title" placeholder="Chainsaw Man" class="rounded-3xl px-4 py-1 bg-neutral-400 placeholder:text-neutral-600 text-black">
                </div>
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="author" class="text-sm ml-2">Author</label>
                    <input type="text" id="author" name="author" placeholder="Tatsuki Fujimoto" class="rounded-3xl px-4 py-1 bg-neutral-400 placeholder:text-neutral-600 text-black">
                </div>
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="status" class="text-sm ml-2">Status</label>
                    <select id="status" name="status" class="rounded-3xl px-4 py-1 bg-neutral-400 text-black">
                        <option value="Ongoing">Ongoing</option>
                        <option value ="Completed">Completed</option>
                    </select>
                </div>
            </div>        
            <div>
                <label for="desc" class="text-sm ml-2">Description</label>
                <textarea id="desc" name="desc" class="w-full rounded-3xl px-4 py-1 bg-neutral-400 text-black h-36 resize-none"></textarea>
            </div>
            <div class="flex flex-row gap-4">
                <label for="cover">Upload the cover photo:</label> 
                <input type="file" id="cover" name="cover" accept="image/png, image/jpeg" class="file:px-4 file:bg-neutral-400 file:text-black file:rounded-3xl file:cursor-pointer"/>
            </div>
            <div class="flex justify-end">
                <button type="submit" form="new-manga" value="Submit" class="px-4 py-1 bg-[#9696c8d9] text-black rounded-3xl">Submit</button>
            </div>
        </div>
    </form>
</section>