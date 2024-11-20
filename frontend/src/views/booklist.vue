<template>
  <div class="content-box-book">
		<div class="empty-state" v-if="prop.bookList.length === 0">
		<div class="empty-box" @click="handleFindBook">
			<p>Click Here</p>
			<ElIcon :size="100"><Collection /></ElIcon>
			<p>Find Your Book!😄</p>
		</div>
		</div>
    <div class="book" v-for="item in prop.bookList" v-else>
      <div class="cover" @click="openBook(item)">
        <img :src="item.cover" alt="" style="width: 100%; height: 100%" />
      </div>
      <div class="title-b">
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts" name="booklist">
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { ElIcon } from 'element-plus';

const router = useRouter();
const prop = reactive({
  bookList: [
    {
      name: "Harry Potter",
      bookid: 1,
      cover: "https://static.posters.cz/image/750webp/214933.webp",
      url:
        "https://ebookpresssite.wordpress.com/wp-content/uploads/2017/10/4_harry_potter_and_the_goblet_of_fire.pdf",
      currentPage: 1,
    },
    {
      name: 'Camp Half-Blood Confidential',
      bookid: 2,
      cover: 'https://www.deseret.com/resizer/v2/ATFKQA4FM3LWBHKMCBROFAKVZI.jpg?auth=2b8187b2b9267632f29a4fdcaaade376326b6e730537b608a2a56cfe24569b8f&focal=389%2C600&width=800&height=600',
      url: 'https://ebookpresssite.wordpress.com/wp-content/uploads/2021/11/camphalf-bloodconfidential.pdf',
      currentPage: 1
    }
  ],
});

const openBook = (data: any) => {
  router.push({
    path: "/bookcontent",
    query: {
      bookurl: "https://corsproxy.io/?" + data.url,
      bookid: data.bookid,
      currentPage: data.currentPage,
      name: data.name,
    },
  });
};
const handleFindBook = () => {
  router.push("/home/recommendation");
};
</script>

<style scoped>
.content-box-book {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
  margin: 0;
  flex-wrap: wrap;
}
.empty-state{
	display: flex;
	flex-direction: column;
	width: 100%;
	justify-content: center;
	align-items: center;
	font-size: 30px;
	font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
.empty-box{
	width: 300px;
	height: 300px;
	cursor: pointer;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	border-radius: 50px;
}
.empty-box:hover{
	color: #409EFF;
	box-sizing: border-box;
  background-clip: padding-box;
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4); 
}
.book {
  width: 150px;
  height: 250px;
  margin: 15px;
}
.cover {
  width: 100%;
  height: 220px;
  border-radius: 15px;
  margin: 0 0 10px 0;
  cursor: pointer;
  overflow: hidden;
}
.cover:hover {
  box-sizing: border-box;
  border: 1px solid transparent;
  background-clip: padding-box;
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4);
}
.title-b {
  display: flex;
  justify-content: center;
  font-family: cursive;
  font-size: 18px;
}
</style>
