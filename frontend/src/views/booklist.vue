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
    },
    {
      name: 'Jane Eyre',
      bookid: 3,
      cover: 'data:image/jpeg;base64,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',
      url: 'https://www.ufmg.br/centrocultural/wp-content/uploads/2020/05/6-Jane-Eyre-Charlotte-Bront%C3%AB.pdf',
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
