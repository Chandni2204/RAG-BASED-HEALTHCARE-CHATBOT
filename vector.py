import faiss

# Load the FAISS index from the .faiss file
index = faiss.read_index('faiss_index1/index.faiss')

# Check how many vectors are in the index
print(f"Number of vectors in the index: {index.ntotal}")


# Retrieve all vectors stored in the index
vectors = index.reconstruct_n(0, index.ntotal)

# Print out the first vector to check
print(vectors)