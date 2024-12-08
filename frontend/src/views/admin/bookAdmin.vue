<template>
  <div class="page-body">
    <div class="menu-bar">
      <ElMenu class="menu-vertical" default-active="1">
        <ElMenuItem index="1" @click="getAllBooks">ALL</ElMenuItem>
        <ElMenuItem
          v-for="(item, index) in journey"
          :index="`${index + 2}`"
          @click="handleSearchCategory(index + 1)"
        >
          <span>{{ item }}</span>
        </ElMenuItem>
      </ElMenu>
    </div>
    <div class="box-container">
      <div class="tool-bar">
        <ElButton
          type="primary"
          style="margin-right: 20px"
          :icon="Plus"
          @click="openDrawer()"
        >
          Create Book
        </ElButton>
      </div>
      <div class="book-containner">
        <div class="book" v-for="book in param.bookList" :key="book.book_id">
          <div class="cover">
            <div class="background">
              <img :src="book.img_url" />
            </div>
            <div class="actions">
              <button class="action-btn edit-btn" @click="openDrawer(book)">Edit</button>
              <button class="action-btn delete-btn" @click="deleteBook(book.book_id)">
                Delete
              </button>
            </div>
          </div>
          <div class="title">{{ book.book_name }}</div>
        </div>
      </div>
    </div>
    <ElDrawer v-model="drawer" title="Book Details" size="30%" direction="rtl">
      <ElForm :model="currentBook" :rules="rules" ref="bookForm" label-width="120px">
        <ElFormItem label="Book Title" prop="book_name">
          <ElInput v-model="currentBook.book_name" placeholder="Enter book title" />
        </ElFormItem>
        <ElFormItem label="Author" prop="author_name">
          <ElInput v-model="currentBook.author_name" placeholder="Enter author name" />
        </ElFormItem>
        <ElFormItem label="Category" prop="category_id">
          <ElSelect v-model="currentBook.category_id" placeholder="Select category">
            <ElOption
              v-for="(category, index) in journey"
              :key="index"
              :label="category"
              :value="index + 1"
            />
          </ElSelect>
        </ElFormItem>
        <ElFormItem label="File URL" prop="file_url">
          <ElInput v-model="currentBook.file_url" placeholder="Enter file URL" />
        </ElFormItem>
        <ElFormItem label="Image URL" prop="img_url">
          <ElInput v-model="currentBook.img_url" placeholder="Enter image URL" />
        </ElFormItem>
        <ElFormItem label="Description" prop="description">
          <ElInput
            v-model="currentBook.description"
            type="textarea"
            placeholder="Enter description"
            autosize
          />
        </ElFormItem>
        <ElFormItem>
          <ElButton type="primary" @click="saveBook">Save</ElButton>
          <ElButton @click="drawer = false">Cancel</ElButton>
        </ElFormItem>
      </ElForm>
    </ElDrawer>
  </div>
</template>

<script setup lang="ts" name="book-admin">
import {
  ElButton,
  ElDrawer,
  ElMenu,
  ElMenuItem,
  ElLoading,
  ElForm,
  ElFormItem,
  ElInput,
  ElSelect,
  ElOption,
} from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import { onMounted, reactive, ref } from "vue";
import {
  getBooks,
  editBook as apiSaveBook,
  deleteBook as apiDeleteBook,
  createBook as apiCreateBook,
} from "../../api";

// Predefined journey categories
const journey = [
  "Literary Fiction",
  "Philosophy",
  "Fantasy",
  "Science Fiction",
  "Poetry",
  "Mystery & Thriller",
  "Biography & Memoirs",
  "Self-Help & Psychology",
  "Historical Fiction",
  "Adventure & Travel",
];

// State and reactive variables
const drawer = ref(false);
const currentBook = reactive({
  book_id: null,
  book_name: "",
  author_name: "",
  file_url: "",
  img_url: "",
  description: "",
  category_id: null,
});
const param = reactive({
  bookList: [],
});
const rules = reactive({
  book_name: [{ required: true, message: "Book title is required", trigger: "blur" }],
  author_name: [{ required: true, message: "Author name is required", trigger: "blur" }],
  category_id: [{ required: true, message: "Category is required", trigger: "blur" }],
  file_url: [{ required: true, message: "File URL is required", trigger: "blur" }],
});
const bookForm = ref(null);

// Loading instance placeholder
let loadingInstance: any = null;

// Function to handle fetching all books
const getAllBooks = async () => {
  try {
    loadingInstance = ElLoading.service({
      lock: true,
      text: "Loading",
      background: "rgba(0, 0, 0, 0.7)",
    });

    const res = await getBooks();
    param.bookList = res.books || []; // Ensure books list exists in response
  } catch (error) {
    console.error("Error fetching books:", error);
  } finally {
    if (loadingInstance) loadingInstance.close();
  }
};

// Function to handle saving or updating a book
const saveBook = () => {
  bookForm.value.validate(async (valid: boolean) => {
    if (valid) {
      try {
        loadingInstance = ElLoading.service({
          lock: true,
          text: "Saving...",
          background: "rgba(0, 0, 0, 0.7)",
        });

        if (currentBook.book_id) {
          // Edit existing book
          await apiSaveBook(currentBook);
        } else {
          // Create new book
          await apiCreateBook({
            book_name: currentBook.book_name,
            book_url: currentBook.file_url,
            author_name: currentBook.author_name,
            img_url: currentBook.img_url,
            description: currentBook.description,
            category_id: currentBook.category_id,
          });
        }

        drawer.value = false;
        getAllBooks();
      } catch (error) {
        console.error("Error saving book:", error);
      } finally {
        if (loadingInstance) loadingInstance.close();
      }
    }
  });
};

const handleSearchCategory = async (id: any) => {
  try {
    loadingInstance = ElLoading.service({
      lock: true,
      text: "Loading",
      background: "rgba(0, 0, 0, 0.7)",
    });

    const res = await getBooks(id); // Fetch books for a specific category
    param.bookList = res.books || [];
  } catch (error) {
    console.error("Error fetching category books:", error);
  } finally {
    if (loadingInstance) loadingInstance.close();
  }
};

// Function to open the drawer (edit or create mode)
const openDrawer = (book: any = null) => {
  if (book) {
    // Edit mode
    currentBook.book_id = book.book_id;
    currentBook.book_name = book.title;
    currentBook.author_name = book.author;
    currentBook.file_url = book.file_url;
    currentBook.img_url = book.img_url;
    currentBook.description = book.description;
    currentBook.category_id = book.category_id;
  } else {
    // Create mode, reset the form
    currentBook.book_id = null;
    currentBook.book_name = "";
    currentBook.author_name = "";
    currentBook.file_url = "";
    currentBook.img_url = "";
    currentBook.description = "";
    currentBook.category_id = null;
  }
  drawer.value = true;
};

// Function to delete a book
const deleteBook = async (id: number) => {
  try {
    loadingInstance = ElLoading.service({
      lock: true,
      text: "Deleting...",
      background: "rgba(0, 0, 0, 0.7)",
    });

    await apiDeleteBook(id);
    getAllBooks();
  } catch (error) {
    console.error("Error deleting book:", error);
  } finally {
    if (loadingInstance) loadingInstance.close();
  }
};

// Lifecycle hook
onMounted(() => {
  getAllBooks(); // Load books on component mount
});
</script>

<style scoped>
.page-body {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: row;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}
.menu-bar {
  height: 100%;
  width: 200px;
  z-index: 999;
}
.menu-vertical {
  height: 100%;
}
.box-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
.tool-bar {
  width: 100%;
  height: 70px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: end;
  position: fixed;
  top: 70px;
  right: 0%;
}
.book-containner {
  width: 100%;
  display: flex;
  flex-direction: row;
  margin-top: 60px;
  flex-wrap: wrap;
  overflow-y: scroll;
}
.book {
  height: 250px;
  width: 150px;
  margin: 15px;
}
.cover {
  width: 100%;
  height: 220px;
  border-radius: 15px;
  margin: 0 0 10px 0;
  position: relative;
  overflow: hidden;
  cursor: pointer;
}
.background {
  width: 100%;
  height: 100%;
  transition: filter 0.3s ease;
}
.background img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.cover:hover .background {
  filter: blur(5px);
}
.actions {
  position: absolute;
  bottom: -50px;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
  transition: transform 0.3s ease, opacity 0.3s ease;
  opacity: 0;
  z-index: 10;
}
.cover:hover .actions {
  transform: translateY(-50px);
  opacity: 1;
}
.action-btn {
  padding: 5px 10px;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}
.edit-btn {
  background-color: #409eff;
  color: white;
}
.edit-btn:hover {
  background-color: #66b1ff;
}
.delete-btn {
  background-color: #f56c6c;
  color: white;
}
.delete-btn:hover {
  background-color: #ff8787;
}
</style>
